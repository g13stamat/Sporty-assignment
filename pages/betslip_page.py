from pages.base_page import BasePage
from helpers.formatting import extract_text, strip_currency, to_float, calculate_payout

class BetSlipPage(BasePage):
    # Locators
    BETSLIP_CONTAINER = "#bet-slip"
    ODDS_MULTIPLIER = ".betSelectionOdds"
    STAKE_INPUT = "#bet-slip-stake-input"
    PAYOUT_VALUE = "#bet-slip-potential-payout"
    PLACE_BET_BUTTON = "#bet-slip-place-bet"
    MATCH_WINNER_TEXT = ".betSelectionMarket"

    # --- Visibility ---
    def wait_until_visible(self, timeout=30000):
        """
        Ensures the betslip is fully rendered and interactive.
        """
        self.log("Waiting for betslip to become visible")
        self.wait_for_page_ready(timeout=timeout)
        self.wait_for_selector(self.BETSLIP_CONTAINER, state="visible", timeout=timeout)
        self.wait_for_selector(self.STAKE_INPUT, state="visible", timeout=timeout)
        self.log("Betslip is visible and ready")

    # --- Odds ---
    def get_odds_multiplier(self) -> float:
        """Returns the numeric odds multiplier displayed in the betslip."""
        raw = self.get_text(self.ODDS_MULTIPLIER)  # e.g. "Odds: 3.25"
        cleaned = raw.replace("Odds:", "").strip()
        odds = to_float(extract_text(cleaned))
        self.log(f"Extracted odds multiplier: {odds}")
        return odds

    # --- Stake ---
    def enter_bet_amount(self, amount: str):
        """
        Types the stake into the input field.
        Includes a visibility wait to avoid freezes.
        """
        self.log(f"Entering bet amount: {amount}")
        self.wait_for_selector(self.STAKE_INPUT, state="visible")
        self.safe_fill(self.STAKE_INPUT, amount)

    def get_bet_amount(self) -> float:
        raw = self.page.locator(self.STAKE_INPUT).input_value()
        amount = to_float(extract_text(raw))
        self.log(f"Current bet amount: {amount}")
        return amount

    # --- Payout ---
    def get_payout_value(self) -> float:
        """
        Reads the payout value after ensuring the element is present.
        """
        self.wait_for_selector(self.PAYOUT_VALUE, state="visible")
        raw = self.get_text(self.PAYOUT_VALUE)
        cleaned = strip_currency(raw)
        payout = to_float(cleaned)
        self.log(f"Displayed payout value: {payout}")
        return payout

    def calculate_expected_payout(self, stake: float, odds: float) -> float:
        expected = calculate_payout(odds, stake)
        self.log(f"Calculated expected payout: {expected}")
        return expected

    # --- Match info ---
    def get_match_winner(self) -> str:
        raw = self.get_text(self.MATCH_WINNER_TEXT)  # e.g. "Match Winner: Home"
        winner = raw.replace("Match Winner:", "").strip()
        self.log(f"Selected match winner: {winner}")
        return winner

    # --- Actions ---
    def place_bet(self):
        """
        Clicks the PLACE BET button after ensuring it is visible and enabled.
        """
        self.log("Placing bet via betslip")
        self.wait_for_selector(self.PLACE_BET_BUTTON, state="visible")
        self.safe_click(self.PLACE_BET_BUTTON)