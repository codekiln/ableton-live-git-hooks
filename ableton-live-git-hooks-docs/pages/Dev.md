alias:: [[Development]], [[Developing alhook]]

- # Docs for how to develop `ableton-live-git-hooks` and [[alhook]]
	- ## [[Dev/Python]]
		- This project uses [[Python/Library/uv]] to manage dependencies, in conjunction with [[mise]]. `mise` manages installation of `uv` and management of the [[Python/Virtual Environment]] with `uv`.
		- To work on or develop this project, you'll likely want to install `mise` to make use of [[PROJECT_ROOT/.mise.toml]] for executing the project's [[mise Tasks]]. See also [[mise/Python/How To/Use mise to set up a virtualenv with uv]] for more info on the general idea.
	- ## [[Dev/Installation]]
		- ### 1 - follow [[mise/How To/Install Mise/The First Time]]
			- Install mise and ensure it is activated
		- ### 2 - use mise to install project tools and dependencies
			- Run `mise install` to install [[uv]] and create a [[Python/Virtual Environment]] with it
			- Run `mise run install-deps-all` to install the [[Python Libraries]].
	- ## [[Dev/Testing]]
		- ### `mise run test`
			- This will run all tests. See [[Dev/Testing]] for details.
	- ## [[Dev/Formatting]]
		-