#!/usr/bin/env python3
"""Block anything company-specific or secret from reaching the public repo.

Scans every file git would publish (tracked + untracked-not-ignored) for:
  - secrets and tokens
  - internal URLs and IDs
  - real email addresses (anything outside example domains)
  - customer names listed in .scrub-denylist.txt (gitignored, one term per line)

Usage: python3 scripts/scrub_check.py        exit 1 on any finding
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DENYLIST = ROOT / ".scrub-denylist.txt"
SKIP_FILES = {"scripts/scrub_check.py"}
ALLOWED_EMAIL_DOMAINS = {"example.com", "acme.com", "example.org", "noreply.anthropic.com"}

PATTERNS = {
    "api key / token": r"(sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|xox[abpr]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,})",
    "bearer token": r"Bearer\s+[A-Za-z0-9._-]{20,}",
    "assigned secret": r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"{}\s]{12,}['\"]",
    "slack webhook": r"hooks\.slack\.com/services/\S+",
    "n8n instance url": r"[a-z0-9-]+\.app\.n8n\.cloud",
    "slack channel id": r"\b[CG]0[A-Z0-9]{8,10}\b",
    "octave oId": r"\b(ca|sa|pe|pr|pl|se|uc|co|pp|rf|mo|mp)_[A-Za-z0-9]{15,}\b",
}
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")


def publishable_files():
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return [p for p in out.splitlines() if p not in SKIP_FILES and (ROOT / p).is_file()]


def load_denylist():
    if not DENYLIST.exists():
        return []
    terms = [t.strip() for t in DENYLIST.read_text().splitlines()]
    return [t for t in terms if t and not t.startswith("#")]


def main():
    denylist = load_denylist()
    if not denylist:
        print("WARN .scrub-denylist.txt missing or empty — customer names are not being checked")
    deny_re = re.compile(r"(?i)\b(" + "|".join(re.escape(t) for t in denylist) + r")\b") if denylist else None
    compiled = {name: re.compile(p) for name, p in PATTERNS.items()}

    findings = []
    for rel in publishable_files():
        try:
            text = (ROOT / rel).read_text()
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for name, rx in compiled.items():
                if rx.search(line):
                    findings.append((rel, lineno, name, line.strip()))
            for m in EMAIL.finditer(line):
                if m.group(1).lower() not in ALLOWED_EMAIL_DOMAINS:
                    findings.append((rel, lineno, "real email", m.group(0)))
            if deny_re and (m := deny_re.search(line)):
                findings.append((rel, lineno, "customer name", m.group(0)))

    for rel, lineno, name, snippet in findings:
        print(f"{rel}:{lineno}  [{name}]  {snippet[:120]}")
    if findings:
        print(f"\nscrub check FAILED: {len(findings)} finding(s)")
        sys.exit(1)
    print("scrub check passed")


if __name__ == "__main__":
    main()
