from pathlib import Path

from ..constants import REPO_ROOT
from .converter import BIN_SUFFIXES, XML_SUFFIXES

SKIP_DIR_NAMES = {"Backup", "Ableton Project Info"}


def _is_skipped(path: Path) -> bool:
    return any(part in SKIP_DIR_NAMES for part in path.parts)


def iter_bin_files(root: Path | None = None) -> list[Path]:
    root = root or REPO_ROOT
    files: list[Path] = []
    for suf in BIN_SUFFIXES:
        for p in root.rglob(f"*{suf}"):
            if not _is_skipped(p):
                files.append(p)
    return files


def iter_xml_files(root: Path | None = None) -> list[Path]:
    root = root or REPO_ROOT
    files: list[Path] = []
    for sfx in XML_SUFFIXES:
        for p in root.rglob(f"*{sfx}"):
            if not _is_skipped(p):
                files.append(p)
    return files


def find_als_files(directory: Path | None = None) -> list[Path]:
    directory = directory or REPO_ROOT
    return list(directory.rglob("*.als"))


def find_als_xml_files(directory: Path | None = None) -> list[Path]:
    directory = directory or REPO_ROOT
    return list(directory.rglob("*.als.xml"))
