"""
Sync Ableton binary files (.als / .alc) in *dirs* with their XML twins.

• Looks for *.als / *.alc under the supplied directories (recursively)
• skips any path that contains "/Backup/" or "/Ableton Project Info/"
• If the XML is missing **or** older than the binary → regenerate it
• Optionally `git add` the XML when --stage is given
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Iterable

from ..constants import REPO_ROOT
from .converter import BIN_SUFFIXES, extract_bin_to_xml

_SKIP_SUBSTRINGS = ("/Backup/", "/Ableton Project Info/")

def _iter_bins(roots: Iterable[Path]) -> Iterable[Path]:
    for root in roots:
        if not root.exists():
            print(f"⚠️  {root} does not exist – skipping", file=sys.stderr)
            continue
        for suf in BIN_SUFFIXES:
            for p in root.rglob(f"*{suf}"):
                if any(s in p.as_posix() for s in _SKIP_SUBSTRINGS):
                    continue
                yield p

def _validate_in_repo(path: Path) -> Path:
    try:
        return path.relative_to(REPO_ROOT)
    except ValueError:
        raise ValueError(
            f"Path '{path}' is outside the repository root '{REPO_ROOT}'. "
            "All paths must be within the repository."
        )

def sync_dirs(dirs: Iterable[str], stage: bool = False) -> None:
    # Validate all directories are in repo first
    for d in dirs:
        _validate_in_repo(Path(d).resolve())

    for bin_path in _iter_bins(Path(d).resolve() for d in dirs):
        xml_path = bin_path.with_suffix(bin_path.suffix + ".xml")
        if not xml_path.exists() or bin_path.stat().st_mtime > xml_path.stat().st_mtime:
            rel_path = _validate_in_repo(bin_path)
            print(f"• extracting {rel_path} → {xml_path.name}")
            extract_bin_to_xml(bin_path)
            if stage:
                git_path = _validate_in_repo(xml_path)
                subprocess.run(["git", "add", str(git_path)], check=False)

def _cli() -> None:
    ap = argparse.ArgumentParser(
        prog="alhook --sync",
        description="Regenerate XML for modified Ableton files",
    )
    ap.add_argument(
        "dirs", nargs="+", help="One or more directories to scan"
    )
    ap.add_argument(
        "--no-stage", action="store_true", help="Do NOT git-add the regenerated XML"
    )
    args = ap.parse_args()
    sync_dirs(args.dirs, stage=not args.no_stage)

if __name__ == "__main__":
    _cli()