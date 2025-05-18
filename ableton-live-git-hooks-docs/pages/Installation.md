# Installing `ableton-live-git-hooks` into your project
	- ## Using [[Python/Library/lefthook]] in a python repository
		- ### Assuming your repository uses [[Python/Library/uv]] or `pip`:
			- #### Install `ableton-live-git-hooks`
				- Eventually, we will be able to have users install like:
					- `uv add --dev ableton-live-git-hooks`
				- For now, though, the only way to install it is to add this project as an editable dependency:
					- Add it as an editable dependency to your project's `pyproject.toml`:
						- ~~~
						  [project]
						  # ... other project settings ...
						  
						  [project.optional-dependencies]
						  dev = [
						      "ableton-live-git-hooks @ git+https://github.com/codekiln/ableton-live-git-hooks.git",
						      # ... other dev dependencies ...
						  ]
						  ~~~
					- Install the development dependencies:
						- ~~~
						  uv pip install -e ".[dev]"
						  ~~~
					- Or if you're using pip:
						- ~~~
						  pip install -e ".[dev]"
						  ~~~
			- #### Install and configure [Lefthook](https://lefthook.dev/installation/python.html)
				- Add Lefthook to your project's development dependencies:
					- ~~~
					  [project.optional-dependencies]
					  dev = [
					      "lefthook>=1.6.0",
					      # ... other dev dependencies ...
					  ]
					  ~~~
				- Install Lefthook:
					- Using uv:
						- ~~~
						  uv pip install lefthook
						  ~~~
					- Or using pip:
						- ~~~
						  pip install lefthook
						  ~~~
				- Initialize Lefthook in your project:
					- ~~~
					  lefthook install
					  ~~~
				- Create a `lefthook.yml` configuration file in your project root:
					- ~~~
					  # lefthook.yml
					  pre-commit:
					    parallel: true
					    commands:
					      ableton-hooks:
					        run: alhook pre-commit {files}
					        glob: "*.{als,alc}"
					  
					  pre-push:
					    parallel: true
					    commands:
					      ableton-hooks:
					    run: alhook pre-push
					  ~~~
				- Optional: Add `lefthook-local.yml` to `.gitignore` for local overrides:
					- ~~~
					  # .gitignore
					  lefthook-local.yml
					  ~~~
				- Note: If you're running in CI, set `CI=true` to prevent Lefthook from installing hooks during postinstall
	- ## Requirements
		- Python >= 3.13 (as specified in [[pyproject.toml]])
		- Git repository with `.als` or `.alc` files
		- For development of `ableton-live-git-hooks`, see: [[Dev/Installation]]