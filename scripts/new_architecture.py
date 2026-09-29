#!/usr/bin/env python3
"""Scaffold a new architecture inside a group from _template/architecture/.

Usage: python3 scripts/new_architecture.py <group-id> <build-id>

Build ids follow <platform>-<job>-<destination> where the pattern fits
(clay-abm-slack, n8n-email-sequencer, llm-callprep). A leading platform token
and a trailing destination token are copied into build.json.
"""
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLATFORMS = {"clay", "cargo", "claude", "n8n", "llm", "trigger"}
DESTINATIONS = {"slack", "salesforce", "hubspot", "custom", "crm"}
KEBAB = r"[a-z0-9]+(-[a-z0-9]+)*"


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: new_architecture.py <group-id> <build-id>")
    group_id, build_id = sys.argv[1], sys.argv[2]
    if not re.fullmatch(KEBAB, build_id):
        sys.exit(f"build-id must be kebab-case: {build_id!r}")

    group_dir = ROOT / "architectures" / group_id
    if not (group_dir / "group.json").exists():
        sys.exit(f"no such group: {group_id} (create it with scripts/new_group.py)")
    dest = group_dir / build_id
    if dest.exists():
        sys.exit(f"already exists: {dest.relative_to(ROOT)}")

    shutil.copytree(ROOT / "_template" / "architecture", dest)

    tokens = build_id.split("-")
    meta_path = dest / "build.json"
    meta = json.loads(meta_path.read_text())
    meta["id"] = build_id
    meta["title"] = " ".join(t.upper() if t in {"abm", "crm", "llm", "n8n"} else t.capitalize() for t in tokens)
    meta["group"] = group_id
    if tokens[0] in PLATFORMS:
        meta["platform"] = tokens[0]
    if tokens[-1] in DESTINATIONS:
        meta["destination"] = tokens[-1]
    meta["last_updated"] = datetime.date.today().isoformat()
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")

    print(f"created {dest.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
