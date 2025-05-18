#!/usr/bin/env python
import stat

from ..constants import (
    GIT_DIR,
    GIT_HOOKS_DIR,
    PACKAGE_GITHOOKS_DIR,
)


def install_hooks():
    """
    Symlink all *.py hooks in PACKAGE_GITHOOKS_DIR to the .git/hooks directory,
    converting underscores to hyphens to match Git's default hook names.
    Example: pre_commit.py -> pre-commit
    """
    if not GIT_DIR.exists():
        raise RuntimeError(f"Git directory does not exist: {GIT_DIR}")
    if not GIT_HOOKS_DIR.exists():
        raise RuntimeError(f"Git hooks directory does not exist: {GIT_HOOKS_DIR}")

    for hook_script in PACKAGE_GITHOOKS_DIR.glob("*.py"):
        # Convert file name: pre_commit.py -> pre-commit
        hook_name = hook_script.stem.replace("_", "-")
        hook_target = GIT_HOOKS_DIR / hook_name

        # Remove existing file or symlink if it exists
        if hook_target.exists() or hook_target.is_symlink():
            hook_target.unlink()

        # Make sure the .py file is executable
        current_mode = hook_script.stat().st_mode
        hook_script.chmod(current_mode | stat.S_IXUSR)

        # Create a symlink in .git/hooks pointing to the actual .py script
        hook_target.symlink_to(hook_script.resolve())

        print(f"Installed hook: {hook_name} -> {hook_script.name}")


if __name__ == "__main__":
    install_hooks()
