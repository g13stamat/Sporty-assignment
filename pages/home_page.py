from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://qae-assignment-tau.vercel.app/?user-id=candidate-5b1a0f3d"

    # Locators
    MATCH_CARD = ".matchCard"
    BADGE = ".matchMeta .badge"
    ODDS_BUTTON = ".oddsButton"

    def __init__(self, page):
        super().__init__(page)
        self._used_match_ids: set[str] = set()

    # --- Navigation ---
    def open(self):
        self.log("Opening Home Page")
        self.navigate(self.URL)
        self.wait_for_page_ready()
        self.wait_for_selector(self.MATCH_CARD, state="visible", timeout=30000)
        self.log("Home Page loaded successfully")

    # --- Match selection ---
    def select_next_upcoming_match(self):
        """Returns match_id and clicks HOME odds by default."""
        self.wait_for_selector(self.MATCH_CARD, state="visible", timeout=30000)

        cards = self.page.locator(self.MATCH_CARD)
        count = cards.count()
        self.log(f"Found {count} match cards on the page")

        for i in range(count):
            card = cards.nth(i)
            badge = card.locator(self.BADGE).inner_text().strip()

            if badge != "UPCOMING":
                continue

            full_id = card.get_attribute("id")
            match_id = self._extract_match_id(full_id)

            if match_id in self._used_match_ids:
                continue

            self._used_match_ids.add(match_id)
            self.log(f"Selected upcoming match: {match_id}")

            return match_id

        raise Exception("No more upcoming matches available.")

    def select_first_upcoming_match(self):
        """Returns the match_id of the first UPCOMING match without clicking anything."""
        self.wait_for_selector(self.MATCH_CARD, state="visible")

        cards = self.page.locator(self.MATCH_CARD)
        count = cards.count()
        self.log(f"Scanning {count} match cards for first UPCOMING match")

        for i in range(count):
            card = cards.nth(i)
            badge = card.locator(self.BADGE).inner_text().strip()

            if badge == "UPCOMING":
                full_id = card.get_attribute("id")
                match_id = self._extract_match_id(full_id)
                self.log(f"Found first upcoming match: {match_id}")
                return match_id

        raise Exception("No UPCOMING match found on the page.")

    # --- Outcome selection helpers ---
    def click_home_odds(self, card):
        self.log("Clicking HOME odds button")
        odds_button = card.locator(self.ODDS_BUTTON).nth(0)
        odds_button.scroll_into_view_if_needed()
        odds_button.wait_for(state="visible", timeout=15000)
        odds_button.click()

    def click_draw_odds(self, card):
        self.log("Clicking DRAW odds button")
        odds_button = card.locator(self.ODDS_BUTTON).nth(1)
        odds_button.scroll_into_view_if_needed()
        odds_button.wait_for(state="visible", timeout=15000)
        odds_button.click()

    def click_away_odds(self, card):
        self.log("Clicking AWAY odds button")
        odds_button = card.locator(self.ODDS_BUTTON).nth(2)
        odds_button.scroll_into_view_if_needed()
        odds_button.wait_for(state="visible", timeout=15000)
        odds_button.click()

    # --- Utility ---
    def get_card_by_id(self, match_id: str):
        return self.page.locator(f"#match-card-{match_id}")

    def _extract_match_id(self, full_id: str) -> str:
        """Extracts the match ID from the DOM element ID."""
        return full_id.replace("match-card-", "")