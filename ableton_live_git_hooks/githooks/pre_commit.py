#!/usr/bin/env python
import subprocess
import sys
from pathlib import Path

from ..als_git.converter import BIN_SUFFIXES
from ..als_git.sync import sync_dirs
from ..constants import REPO_ROOT

def _staged_bins() -> list[Path]:
    res = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--"]
        + [f"*{s}" for s in BIN_SUFFIXES],
        capture_output=True,
        text=True,
        check=False,
    )
    return [REPO_ROOT / p for p in res.stdout.splitlines() if p.strip()]

def main() -> None:
    bins = _staged_bins()
    if not bins:
        sys.exit(0)
    # use the sync helper but pass individual parent dirs (duplicates fine)
    sync_dirs({b.parent for b in bins}, stage=True)

if __name__ == "__main__":
    main()