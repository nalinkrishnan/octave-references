#!/usr/bin/env python3
"""Scaffold a new architecture group from _template/group/.

Usage: python3 scripts/new_group.py <group-id> ["Group title"]
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit('usage: new_group.py <group-id> ["Group title"]')
    group_id = sys.argv[1]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", group_id):
        sys.exit(f"group-id must be kebab-case: {group_id!r}")
    title = sys.argv[2] if len(sys.argv) == 3 else group_id.replace("-", " ").title()

    dest = ROOT / "architectures" / group_id
    if dest.exists():
        sys.exit(f"already exists: {dest.relative_to(ROOT)}")
    shutil.copytree(ROOT / "_template" / "group", dest)

    meta_path = dest / "group.json"
    meta = json.loads(meta_path.read_text())
    meta["id"], meta["title"] = group_id, title
    meta_path.write_text(json.dumps(meta, indent=2) + "\n")

    doc = dest / "GROUP.md"
    doc.write_text(doc.read_text().replace("{{Group title}}", title))

    print(f"created {dest.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
