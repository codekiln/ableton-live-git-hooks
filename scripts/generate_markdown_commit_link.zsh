#!/usr/bin/env zsh

# Purpose: Generate a Markdown link for the most recent Git commit, including date/time.
# Example: [2024-12-19 11:57 - abc12345 - Fix login bug](https://github.com/username/repo/commit/abc12345) #git/commit
#
# Note: This version uses git's built-in date formatting rather than `date -d`,
# to ensure compatibility with systems like macOS where `date -d` isn't available.

# Parse arguments
SHORT_MODE=false

while [[ "$1" != "" ]]; do
    case $1 in
        --)
            ;;
        --help)
            cat <<EOF
generate_markdown_commit_link.zsh - Generate a Markdown link for the most recent Git commit.
USAGE:
  zsh generate_markdown_commit_link.zsh [--help] [--short]
OPTIONS:
  --help      Display this help information.
  --short     Output only the short SHA link without the commit message or date/time.
EOF
            exit 0
            ;;
        --short)
            SHORT_MODE=true
            ;;
        *)
            echo "Error: Unknown option '$1'. Use --help for usage information." >&2
            exit 1
            ;;
    esac
    shift
done

# Get repository URL and convert SSH to HTTPS
REPO_URL=$(git config --get remote.origin.url)
if [[ "$REPO_URL" =~ ^git@ ]]; then
    REPO_URL=$(echo "$REPO_URL" | sed -E 's|git@([^:]+):|https://\1/|')
fi
REPO_URL=$(echo "$REPO_URL" | sed 's/\.git$//')

# Get commit details
COMMIT_SHA=$(git log -1 --pretty=format:"%h" --abbrev=8)
COMMIT_MSG=$(git log -1 --pretty=format:"%s" | cut -c 1-72)
COMMIT_DATE=$(git log -1 --pretty=format:"%cd" --date=format:'%Y-%m-%d %H:%M')

# Output result
if $SHORT_MODE; then
    echo "$REPO_URL/commit/$COMMIT_SHA"
else
    echo "[$COMMIT_DATE - $COMMIT_SHA - $COMMIT_MSG]($REPO_URL/commit/$COMMIT_SHA) #git/commit"
fi 