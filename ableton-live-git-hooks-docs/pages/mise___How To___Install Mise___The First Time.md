tags:: [[Diataxis/How To]]
logseq-url:: logseq://graph/logseq-encode-garden?page=mise%2FHow%20To%2FInstall%20Mise%2FThe%20First%20Time

- # How to Install Mise for the First Time
	- ## Goal
		- Install and configure mise, a tool for managing programming language runtimes and development tools, for use with this project.
	- ## Preconditions
		- A Unix-like operating system (macOS, Linux, or WSL)
		- Basic familiarity with the command line
		- Git installed (for project development)
	- ## Procedure
		- ### 1. Install the mise CLI
			- Run the following command in your terminal:
				- ~~~
				  curl https://mise.run | sh
				  ~~~
			- This will install mise to `~/.local/bin/mise`
			- Verify the installation:
				- ~~~
				  ~/.local/bin/mise --version
				  ~~~
		- ### 2. Choose an Activation Method
			- #### Option A: Project-Specific Setup (Recommended for First-Time Users)
				- This option is best if you want to try mise with just this project first
				- No shell configuration changes required
				- You'll need to prefix commands with `mise exec` or use `mise run`
				- Example:
					- ~~~
					  mise exec -- python --version
					  ~~~
			- #### Option B: Global Setup (Recommended for Regular Users)
				- This option makes mise available system-wide
				- Add the following to your shell's configuration file:
					- For bash (`~/.bashrc`):
						- ~~~
						  echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc
						  ~~~
					- For zsh (`~/.zshrc`):
						- ~~~
						  echo 'eval "$(~/.local/bin/mise activate zsh)"' >> ~/.zshrc
						  ~~~
					- For fish (`~/.config/fish/config.fish`):
						- ~~~
						  echo '~/.local/bin/mise activate fish | source' >> ~/.config/fish/config.fish
						  ~~~
				- Restart your shell or source your configuration file
				- Verify activation:
					- ~~~
					  mise --version
					  ~~~
				- Next step in this case: [[mise/How To/Install Mise/Shell Completions in Zsh]]
		- ### 3. Configure for This Project
			- The project uses a `mise.toml` configuration file to manage tools and tasks
			- See [[mise/Config/mise.toml]] for details about the project's configuration
			- For Python development setup, see [[mise/Python/How To/Use mise to set up a virtualenv with uv]]
	- ## Troubleshooting
		- ### Installation Issues
			- If the curl command fails, try downloading the binary directly from [mise releases](https://github.com/jdx/mise/releases)
			- Ensure `~/.local/bin` is in your PATH
		- ### Activation Issues
			- If `mise` command is not found after activation:
				- Check that the activation line was added correctly to your shell config
				- Verify the path to mise binary (`~/.local/bin/mise`)
				- Try restarting your shell
		- ### Project-Specific Issues
			- If mise doesn't pick up project configuration:
				- Run `mise config ls` to see which config files are active
				- Ensure you're in the project root directory
	- ## Next Steps
		- For development setup, see [[Dev/Installation]]
		- For Python-specific setup, see [[mise/Python/How To/Use mise to set up a virtualenv with uv]]
		- For task management, see [[mise/Tasks]]
	- ## References
		- [Official mise documentation](https://mise.jdx.dev/)
		- [mise installation guide](https://mise.jdx.dev/installing-mise.html)
		- [mise configuration guide](https://mise.jdx.dev/configuration.html)