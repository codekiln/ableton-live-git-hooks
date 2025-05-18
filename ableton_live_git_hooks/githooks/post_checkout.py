#!/usr/bin/env python
import shutil

from ..als_git.converter import xml_to_bin
from ..als_git.finders import iter_xml_files
from ..constants import REPO_ROOT

def clean_pycache() -> None:
    for p in REPO_ROOT.rglob("__pycache__"):
        shutil.rmtree(p, ignore_errors=True)
    for p in REPO_ROOT.rglob("*.py[co]"):
        p.unlink(missing_ok=True)

def main() -> None:
    clean_pycache()
    for xml in iter_xml_files():
        rebuilt = xml_to_bin(xml)
        print(f"Re-created {rebuilt}")

if __name__ == "__main__":
    main()