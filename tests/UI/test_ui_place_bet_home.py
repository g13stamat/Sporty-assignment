import pytest
from pages.home_page import HomePage
from pages.betslip_page import BetSlipPage

@pytest.mark.ui
def test_ui_place_bet_home(page):
    # --- Arrange ---
    home = HomePage(page)
    home.open()

    # Select next UPCOMING match
    match_id = home.select_next_upcoming_match()
    card = home.get_card_by_id(match_id)

    # --- Act ---
    # Click HOME odds to open the betslip
    home.click_home_odds(card)

    betslip = BetSlipPage(page)
    betslip.wait_until_visible()

    # Enter stake
    stake = 10.0
    betslip.enter_bet_amount(str(stake))

    # --- Assert ---
    # Validate betslip values
    assert betslip.get_match_winner() == "Home"

    odds = betslip.get_odds_multiplier()
    payout = betslip.get_payout_value()
    expected = betslip.calculate_expected_payout(stake, odds)

    assert payout == expected