# tags:: [[Diataxis/Explanation]]

# Development - Formatting and Code Style
	- # Overview
		- This project uses [[Python/Library/Ruff]] to perform code formatting and import sorting, leveraging built-in support for [[Python/Library/black]]-style formatting and [[Python/Library/isort]]-style import ordering via the [[mise Tasks]] defined in [[PROJECT_ROOT/.mise.toml]].

	- # Configuration
		- ## Dependencies
			- Ensure `pyproject.toml` dev extras include formatting libraries:
			  ~~~toml
			  dev = [
			      "pytest>=8.3.5",
			      "black",
			      "isort",
			  ]
			  ~~~
			- Install formatting libraries into the virtual environment:
			  ```shell
			  mise run install-deps-dev
			  ```
		- ## Ruff configuration
			- Define a `[tool.ruff]` section in `pyproject.toml` or a standalone `.ruff.toml` to customize formatting rules, for example:
			  ~~~toml
			  [tool.ruff]
			  line-length = 88
			  select = ["I"]         # import-sorting rules
			  fixable = ["I"]        # enable auto-fixing for import-sorting
			  extend-ignore = ["E501"]  # adjust as needed for project style
			  ~~~

		- ## isort and black integration
			- Optionally configure [[Python/Library/isort]] and [[Python/Library/black]] in `pyproject.toml`:
			  ~~~toml
			  [tool.isort]
			  profile = "black"

			  [tool.black]
			  line-length = 88
			  target-version = ["py313"]
			  ~~~

	- # Usage
		- ## Running lint and format
			- `mise run lint` → runs `ruff check ./ableton_live_git_hooks`
			- `mise run format` → runs `ruff format ./ableton_live_git_hooks`

		- ## On demand
			- Apply formatting to a specific file or directory:
			  ```shell
			  mise run format -- path/to/module.py
			  ```

	- # IDE Integration (optional)
		- To enable on-save formatting in VSCode, add to your workspace settings:
		  ```json
		  {
		    "editor.codeActionsOnSave": {
		      "source.organizeImports": true,
		      "source.fixAll.ruff": true
		    }
		  }
		  ```

	- # Best Practices
		- Run `mise run format` before committing code.
		- Review automatic fixes from `ruff format` to understand changes.
		- Keep your formatting configuration under version control (e.g., `pyproject.toml`).

	- # Related Documentation
		- [[mise/Tasks]] — available mise tasks including `lint` and `format`
		- [[Python/Library/Ruff]] — ruff documentation
		- [[Python/Library/black]] — black documentation
		- [[Python/Library/isort]] — isort documentation