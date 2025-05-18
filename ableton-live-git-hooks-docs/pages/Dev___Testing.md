tags:: [[Diataxis/Explanation]]

# Development - Testing Conventions
	- # Overview
		- This project uses [pytest](https://docs.pytest.org/) for testing, with a focus on clear organization and maintainable test suites.
		- Tests are organized into unit and integration tests, with clear separation of concerns.
		- All tests are run using mise: `mise run test`

	- # Directory Structure
		- ## Test Organization
			- `tests/` - Root test directory
				- `integration/` - Integration tests
					- Mirrors the module structure (e.g., `als_git/` for `ableton_live_git_hooks/als_git/`)
					- `fixtures/` - Test fixtures (e.g., sample `.als` and `.alc` files)
					- `conftest.py` - Shared fixtures for integration tests
				- `unit/` - Unit tests
					- Mirrors the package structure for easy test discovery
					- Each module's tests are in a corresponding test directory

		- ## Naming Conventions
			- Test files: `test_*.py`
			- Test functions: `test_*`
			- Test classes: `Test*`
			- Fixture files: `conftest.py`
			- Test fixtures: Descriptive names ending in `_fixture` or `_fixture_*`

	- # Test Categories
		- ## Integration Tests
			- Marked with `@pytest.mark.integration`
			- Test interactions between components
			- May use real files (e.g., `.als` and `.alc` files)
			- Run with: `mise run test-integration`
			- Located in `tests/integration/`

		- ## Unit Tests
			- Marked with `@pytest.mark.unit`
			- Test individual components in isolation
			- Use mocks and stubs instead of real files
			- Run with: `mise run test-unit`
			- Located in `tests/unit/`

	- # Fixtures
		- ## Integration Test Fixtures
			- Stored in `tests/integration/fixtures/`
			- Shared via `tests/integration/conftest.py`
			- Scoped to integration tests only
			- Example:
				```python
				@pytest.fixture
				def ableton_fixture_path(request) -> Path:
				    """Path to a sample Ableton file for integration tests."""
				    return Path(__file__).parent / "fixtures" / request.param
				```

		- ## Unit Test Fixtures
			- Stored in `tests/unit/conftest.py`
			- Scoped to unit tests only
			- Use mocks and stubs instead of real files

	- # Running Tests
		- ## Basic Usage
			- All tests: `mise run test`
			- Integration only: `mise run test-integration`
			- Unit only: `mise run test-unit`
			- Verbose output: `mise run test -- -v`
			- Specific test file: `mise run test -- tests/integration/als_git/test_converter_integration.py`

		- ## Test Configuration
			- Configured in `pyproject.toml` under `[tool.pytest.ini_options]`
			- Includes test paths, markers, and default options
			- Example:
				```toml
				[tool.pytest.ini_options]
				testpaths = ["tests"]
				python_files = ["test_*.py"]
				markers = [
				    "integration: marks tests as integration tests",
				    "unit: marks tests as unit tests"
				]
				```

	- # Best Practices
		- Keep test files focused and small
		- Use descriptive test names that explain the behavior being tested
		- Use fixtures for setup and teardown
		- Keep integration test fixtures in `tests/integration/fixtures/`
		- Use appropriate markers (`@pytest.mark.integration` or `@pytest.mark.unit`)
		- Write tests that are independent and can run in any order
		- Use meaningful assertions with descriptive failure messages
	- # Related Documentation
		- [[mise/Python/How To/Use mise to set up a virtualenv with uv]] - Project Python setup
		- [[mise/Tasks]] - Available mise tasks
		- [pytest documentation](https://docs.pytest.org/) - Testing framework docs