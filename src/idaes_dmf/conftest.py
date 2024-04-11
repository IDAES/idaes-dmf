import pytest


MARKERS = {
    "unit": "quick tests that do not require a solver, must run in <2s",
    "component": "quick tests that may require a solver",
    "integration": "long duration tests",
    "performance": "tests for the IDAES performance testing suite",
    "linux": "tests that should only run on Linux",
}


def pytest_configure(config: pytest.Config):
    for name, description in MARKERS.items():
        config.addinivalue_line("markers", f"{name}: {description}")
