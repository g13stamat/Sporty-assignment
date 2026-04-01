from pages.base_page import BasePage
from helpers.formatting import extract_text, strip_currency, to_float, round2, calculate_payout

class BetPopupPage(BasePage):
    # Locators
    MODAL = ".modalBody"
    TITLE = ".modalTitle"
    BET_ID = "#modal-success-bet-id"
    MATCH = "#modal-success-match"
    STAKE = "#modal-success-stake"
    ODDS = "#modal-success-odds"
    PAYOUT = "#modal-success-payout"
    CLOSE_BUTTON = ".modalCloseButton"

    # --- Visibility ---
    def wait_for_visible(self, timeout=15000):
        self.log("Waiting for bet confirmation popup")
        self.wait_for_selector(self.MODAL, state="visible", timeout=timeout)
        self.log("Bet confirmation popup is visible")

    # --- Text getters ---
    def get_title(self) -> str:
        title = self.get_text(self.TITLE)
        self.log(f"Popup title: {title}")
        return title

    def get_bet_id(self) -> str:
        bet_id = self.get_text(self.BET_ID)
        self.log(f"Bet ID: {bet_id}")
        return bet_id

    def get_match(self) -> str:
        match = self.get_text(self.MATCH)
        self.log(f"Match text: {match}")
        return match

    def get_stake(self) -> float:
        raw = self.get_text(self.STAKE)  # e.g. "€2.00"
        cleaned = strip_currency(raw)
        stake = to_float(cleaned)
        self.log(f"Stake shown in popup: {stake}")
        return stake

    def get_odds(self) -> float:
        raw = self.get_text(self.ODDS)  # e.g. "2.35"
        cleaned = extract_text(raw)
        odds = to_float(cleaned)
        self.log(f"Odds shown in popup: {odds}")
        return odds

    def get_payout(self) -> float:
        raw = self.get_text(self.PAYOUT)  # e.g. "€4.00"
        cleaned = strip_currency(raw)
        payout = to_float(cleaned)
        self.log(f"Payout shown in popup: {payout}")
        return payout

    # --- Validation ---
    def validate_payout(self, stake_amount: str):
        """Validates that the popup payout matches the expected calculation."""
        stake = to_float(stake_amount)
        odds = self.get_odds()
        expected = calculate_payout(odds, stake)
        actual = round2(self.get_payout())

        self.log(f"Validating payout: expected={expected}, actual={actual}")

        assert actual == expected, (
            f"Modal payout mismatch: expected {expected}, got {actual}. "
            f"(odds={odds}, stake={stake})"
        )

    # --- Actions ---
    def close(self):
        self.log("Closing bet confirmation popup")
        self.safe_click(self.CLOSE_BUTTON)