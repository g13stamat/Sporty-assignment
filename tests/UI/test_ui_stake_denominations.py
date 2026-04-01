import pytest
from helpers.formatting import to_float
from pages.home_page import HomePage
from pages.betslip_page import BetSlipPage

@pytest.mark.ui
@pytest.mark.parametrize("stake_amount", [
    "1.0",
    "1.00",
    "1.01",
    "1.99",
    "10.00",
    "99.99",
    "100.00",
])
def test_ui_payout_calculation(page, stake_amount):
    # --- Arrange ---
    home = HomePage(page)
    home.open()

    # Select next UPCOMING match
    match_id = home.select_next_upcoming_match()
    card = home.get_card_by_id(match_id)

    # --- Act ---
    # Click HOME odds
    home.click_home_odds(card)

    betslip = BetSlipPage(page)
    betslip.wait_until_visible()

    odds = betslip.get_odds_multiplier()

    # Enter stake
    betslip.enter_bet_amount(stake_amount)

    # --- Assert ---
    expected = betslip.calculate_expected_payout(to_float(stake_amount), odds)
    actual = betslip.get_payout_value()

    assert actual == expected