"""
Integration test fixtures.
"""
from pathlib import Path

import pytest


@pytest.fixture
def ableton_fixture_path(request) -> Path:
    """Path to a sample Ableton file for integration tests."""
    return Path(__file__).parent / "fixtures" / request.param