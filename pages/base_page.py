import logging
from datetime import datetime

class BasePage:
    """Shared UI helpers for all page objects."""

    def __init__(self, page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    # --- Logging helper ---
    def log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logger.info(f"[{timestamp}] {message}")

    # --- Navigation ---
    def navigate(self, url: str):
        self.log(f"Navigating to: {url}")
        self.page.goto(url)

    # --- Safe actions ---
    def safe_click(self, locator: str):
        self.log(f"Clicking: {locator}")
        self.page.locator(locator).first.wait_for(state="visible")
        self.page.locator(locator).first.click()

    def safe_fill(self, locator: str, text: str):
        self.log(f"Filling '{locator}' with '{text}'")
        self.page.locator(locator).first.wait_for(state="visible")
        self.page.locator(locator).first.fill(text)

    def get_text(self, locator: str) -> str:
        self.page.locator(locator).first.wait_for(state="visible")
        text = self.page.locator(locator).first.inner_text()
        self.log(f"Read text from '{locator}': {text}")
        return text

    # --- Wait helpers ---
    def wait_for_selector(self, locator: str, state="visible", timeout=15000):
        self.log(f"Waiting for selector '{locator}' to be {state}")
        self.page.locator(locator).first.wait_for(state=state, timeout=timeout)

    def wait_for_page_ready(self, timeout=30000):
        """Wait only for initial DOM load. SPA pages never reach full idle state."""
        self.log("Waiting for initial DOM to load")
        self.page.wait_for_load_state("domcontentloaded", timeout=timeout)