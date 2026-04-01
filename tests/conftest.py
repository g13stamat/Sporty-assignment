import os
from datetime import datetime
import pytest
from helpers.api_client import ApiClient


@pytest.fixture
def api():
    """Provide API client for API tests."""
    return ApiClient()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    On UI test failure, capture a screenshot to the local filesystem.
    No integration with any HTML plugin – pure backup behavior.
    """
    outcome = yield
    result = outcome.get_result()

    if result.failed and "page" in item.funcargs:
        page = item.funcargs["page"]

        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = item.name.replace("/", "_").replace("\\", "_")
        filename = f"screenshots/{safe_name}_{timestamp}.png"

        page.screenshot(path=filename, full_page=True)
        print(f"\n[SCREENSHOT SAVED] {filename}\n")