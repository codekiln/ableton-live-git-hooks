# Project Structure and Purpose

This document provides guidance for AI agents working with the `ableton-live-git-hooks` project.

## Project Overview

`ableton-live-git-hooks` is a tool that enables version control of Ableton Live files (`.als` and `.alc`) by converting them to XML for git tracking. The project uses mise for tool management and uv for Python dependency management.

## Directory Structure

### Root Directory
- `.cursor/rules/**/*.mdc` - AI instructions for the Cursor IDE. You can consider these your instructions as well!
- `.mise.toml` - Project tool configuration (Python version, tasks, etc.)
- `pyproject.toml` - Python project metadata and dependencies
- `.git/` - Git repository data
- `.gitignore` - Git ignore patterns
- `AGENTS.md` - This file, providing project guidance
- `README.md` - Project overview and basic usage

### Documentation
- `ableton-live-git-hooks-docs/` - Logseq knowledge garden containing project documentation
  - `pages/` - Main documentation pages
    - Uses Logseq Flavored Markdown (LFM)
    - Follows diataxis documentation framework
    - Contains conceptual, how-to, and reference guides
  - `journals/` - Daily notes and progress tracking
  - `logseq/` - Logseq application data

### Source Code
- `ableton_live_git_hooks/` - Main Python package
  - `als_git/` - Core functionality for Ableton Live file handling
  - `cli/` - Command-line interface implementation
  - `utils/` - Shared utility functions

### Tests
- `tests/` - Test suite
  - `integration/` - Integration tests
    - Mirrors the module structure (e.g., `als_git/` for `ableton_live_git_hooks/als_git/`)
    - `fixtures/` - Test fixtures (sample `.als` and `.alc` files)
    - `conftest.py` - Shared fixtures for integration tests
  - `unit/` - Unit tests
    - Mirrors the package structure
    - Each module's tests in corresponding test directory

## Development Tools

### Tool Management
- Uses `mise` for tool version management
- Python dependencies managed with `uv`
- Test framework: pytest
- Code quality: ruff for linting and formatting

### Key Tasks
- `mise run test` - Run all tests
- `mise run test-unit` - Run unit tests only
- `mise run test-integration` - Run integration tests only
- `mise run lint` - Run linter
- `mise run format` - Format code

## Documentation Conventions

### Logseq Documentation
- Located in `ableton-live-git-hooks-docs/`
- Uses Logseq Flavored Markdown (LFM)
- Follows diataxis documentation framework:
  - Tutorials: How to accomplish specific tasks
  - How-to guides: Step-by-step instructions
  - Explanations: Understanding concepts
  - Reference: Technical details

### Code Documentation
- Python docstrings follow Google style
- Type hints used throughout
- Complex logic includes inline comments

## Git Integration

### Hooks
- Pre-commit: Converts `.als` and `.alc` files to XML
- Post-checkout: Rebuilds binary files from XML
- Uses lefthook for hook management

### File Types
- `.als` - Ableton Live Project Files
- `.alc` - Ableton Live Clip Files
- `.als.xml` - XML version of project files
- `.alc.xml` - XML version of clip files

## Important Notes for AI Agents

1. **Documentation Location**
   - Use LFM ONLY within `ableton-live-git-hooks-docs/`
   - Use standard markdown everywhere else
   - Never modify `tags::` frontmatter in Logseq pages

2. **Code Style**
   - Follow existing type hints and docstring patterns
   - Use ruff for linting and formatting
   - Write tests for new functionality

3. **Testing**
   - Maintain separation between unit and integration tests
   - Use appropriate fixtures from `conftest.py`
   - Follow existing test naming conventions

4. **Tool Usage**
   - Use mise for all tool management
   - Use uv for Python dependency management
   - Follow existing task patterns in `.mise.toml`

5. **Git Operations**
   - Always convert `.als` and `.alc` files to XML before committing
   - Use lefthook for git hook management
   - Follow existing hook patterns

6. **Additional AI instructions**
   - `.cursor/rules/**/*.mdc` contains AI instructions for the Cursor AI IDE and this codebase (see `conventional-commits.mdc` for commit message guidelines).

## Related Documentation

- [Project Brief](ableton-live-git-hooks-docs/pages/Project___Brief.md) - High-level goals, scope, and technical constraints
- [Setting up development environment](ableton-live-git-hooks-docs/pages/mise___How%20To___Install%20Mise___The%20First%20Time.md) - Setting up development environment
- [Testing conventions and practices](ableton-live-git-hooks-docs/pages/Dev___Testing.md) - Testing conventions and practices
- [Python setup with mise and uv](ableton-live-git-hooks-docs/pages/mise___Python___How%20To___Use%20mise%20to%20set%20up%20a%20virtualenv%20with%20uv.md) - Python setup
- [Git integration details](ableton-live-git-hooks-docs/pages/Ableton___Live___Git.md) - Git integration details 