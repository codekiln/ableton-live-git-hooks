# CLI UX Briefing: `alhook` with Git Clean and Smudge Filters
	- ## 1. Purpose & Context
		- This briefing outlines the user experience for the `alhook` CLI when leveraging Git's clean/smudge filter driver to manage Ableton Live `.als` and `.alc` files as sidecar XML in your Git repository. It captures:
			- Sequential installation steps
			- Runtime workflows for both CLI and IDE environments
			- Verification of `alhook` availability for Git filters
			- Mitigation of environment mismatches (e.g., VSCode's Git integration)
	- ## 2. Scope
		- **In-Scope:**
			- `alhook install-filter` command to scaffold `.gitattributes` and Git filter config
			- User workflows: modify, stage, commit, and checkout
			- Checks for `alhook` in Git's `$PATH` (CLI and IDE)
		- **Out-of-Scope:**
			- Alternative workflows (e.g., Lefthook-based approaches)
			- Non-Ableton file patterns
	- ## 3. [[Installation]] Sequence Proposal
		- **Install Dependencies**
			- ~~~
			  pip install ableton-live-git-hooks
			  ~~~
		- **Verify CLI in PATH**
			- ~~~
			  which alhook     # should return a valid path
			  alhook --version # confirms executable works
			  ~~~
		- **Run Filter Installer**
			- ~~~
			  alhook install-filter
			  ~~~
			- Appends to `.gitattributes`:
				- ~~~
				  *.als filter=ableton
				  *.alc filter=ableton
				  ~~~
			- Writes to `.git/config` under `[filter "ableton"]`:
				- ~~~
				  clean  = alhook export --xml --stdin
				  smudge = alhook import --binary --stdin
				  ~~~
			- Provides confirmation messages:
				- "Updated .gitattributes"
				- "Configured Git filter 'ableton' in .git/config"
	- ## 4. Runtime Workflow Proposal
		- **Modify Project**
			- Open `song.als` in Ableton, make edits.
		- **Stage & Commit**
			- ~~~
			  git add song.als      # Git invokes clean filter → generates XML sidecar
			  git commit -m "Update song structure"
			  ~~~
			- Under the hood:
				- **clean filter**: `alhook export --xml --stdin` transforms binary to XML in the index
				- **commit** writes XML to history
		- **Checkout / Clone**
			- ~~~
			  git checkout <branch>
			  ~~~
			- **smudge filter**: `alhook import --binary --stdin` reconstructs `.als` in working tree
	- ## 5. Verifying `alhook` Availability
		- **CLI Check:** `which alhook` and `alhook --version` before filter installation.
		- **IDE Integration:** VSCode's Git extension must inherit the same `$PATH`:
			- Recommend adding a `.env` file at project root with `PATH` adjustments.
			- Or use a VSCode setting: `"git.path": "/usr/local/bin/git"` and ensure `/usr/local/bin` includes your Python environment's bin.
		- **Fallback Warning:** If filter runs fail, Git will display errors. `alhook install-filter` should record a pre-install validation step and abort if `alhook` isn't found.
	- ## 6. IDE Considerations & Mitigations
		- **Problem:** VSCode's embedded Git may use a different shell or PATH, leading to filter lookup failures.
		- **Mitigations:**
			- **Include Shebang:** Package `alhook` with a shebang (`#!/usr/bin/env python3`) so Git's shell can execute it.
			- **Wrapper Script:** During `install-filter`, generate a small executable wrapper in `.git/hooks` directory that invokes the correct Python interpreter explicitly.
			- **Documentation Note:** In `README.md`, add a section under "IDE Setup" explaining how to align VSCode's Git PATH with the system environment.
	- ## 7. Next Steps
		- Prototype `alhook install-filter` implementation.
		- Test end-to-end on macOS (CLI & VSCode).
		- Gather feedback on clarity of setup instructions and error messaging.
		- Iterate on wrapper script approach if PATH issues persist.