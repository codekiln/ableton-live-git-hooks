tags:: [[Diataxis/Explanation]]

# Development - Commit Message Guidelines
	- # Overview
		- Write clear, consistent Git commit messages following the Conventional Commits specification.
		- Good commit messages improve project history readability and tool interoperability.

	- # Commit Message Format
		- Use the following structure:

			```text
			<type>(<scope>): <subject>

			<body>

			<footer>
			```

		- **type**: one of `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, etc.
		- **scope**: optional component or file name.
		- **subject**: short description (imperative, max 72 characters).
		- **body**: detailed description (wrap at 80 characters).
		- **footer**: references to issues or breaking changes.

	- # Guidelines
		- Use present tense and imperative mood (e.g., "Add feature", not "Added feature").
		- Limit subject line to 50 characters if not using a scope; wrap at 72 when including a scope.
		- Separate subject from body with a blank line.
		- Use the footer to reference issue numbers (e.g., `Closes #123`) or breaking changes (`BREAKING CHANGE: description`).
		- Prefix merge commits with `chore` (e.g., `chore: merge branch '...'`).

	- # Examples
		- `feat(parser): support new syntax for ..`
		- `fix(cli): handle missing config file`
		- `docs: update README with usage examples`
		- `chore: bump version to 1.2.0`

	- # Further Reading
		- See the full specification in `.cursor/rules/conventional-commits.mdc`.