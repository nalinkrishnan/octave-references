#!/usr/bin/env python3
"""Scaffold a new architecture from _template/.

Usage: python3 scripts/new_architecture.py <build-id>
"""
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: new_architecture.py <build-id>")
    build_id = sys.argv[1]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", build_id):
        sys.exit(f"build-id must be kebab-case: {build_id!r}")

    dest = ROOT / "architectures" / build_id
    if dest.exists():
        sys.exit(f"already exists: {dest.relative_to(ROOT)}")

    shutil.copytree(ROOT / "_template", dest)

    meta_path = dest / "build.json"
    meta = json.loads(meta_path.read_text())
    meta["id"] = build_id
    meta["last_updated"] = datetime.date.today().isoformat()
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")

    print(f"created {dest.relative_to(ROOT)}/ — fill in build.json first, then README/ARCHITECTURE/SETUP")


if __name__ == "__main__":
    main()
