from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = REPO_ROOT / "ableton_live_git_hooks"
PACKAGE_GITHOOKS_DIR = PACKAGE_ROOT / "githooks"
GIT_DIR = REPO_ROOT / ".git"
GIT_HOOKS_DIR = GIT_DIR / "hooks"
