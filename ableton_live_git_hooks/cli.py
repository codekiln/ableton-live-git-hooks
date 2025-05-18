"""
Command-line interface for Ableton Live Git Hooks.
"""

import argparse
import sys

from .als_git.sync import sync_dirs
from .githooks.install_hooks import install_hooks
from .githooks.pre_commit import main as pre_commit_main
from .githooks.post_checkout import main as post_checkout_main


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="alhook", description="Manage Ableton Live git hooks and file sync"
    )
    parser.add_argument(
        "--install-hooks",
        action="store_true",
        help="Install git hook symlinks into .git/hooks",
    )
    parser.add_argument(
        "--pre-commit",
        dest="pre_commit",
        action="store_true",
        help="Run the pre-commit hook logic",
    )
    parser.add_argument(
        "--post-checkout",
        dest="post_checkout",
        action="store_true",
        help="Run the post-checkout hook logic",
    )
    parser.add_argument(
        "--sync",
        nargs="+",
        metavar="DIR",
        help="Sync .als/.alc files to .xml under given directories",
    )
    parser.add_argument(
        "--no-stage",
        action="store_true",
        help="When syncing, do not stage regenerated XML files",
    )
    args = parser.parse_args()

    if args.install_hooks:
        install_hooks()
    if args.pre_commit:
        pre_commit_main()
    if args.post_checkout:
        post_checkout_main()
    if args.sync:
        sync_dirs(args.sync, stage=not args.no_stage)

    if not (args.install_hooks or args.pre_commit or args.post_checkout or args.sync):
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
