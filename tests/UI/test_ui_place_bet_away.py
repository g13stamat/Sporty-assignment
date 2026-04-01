import pytest
from pages.home_page import HomePage
from pages.betslip_page import BetSlipPage

@pytest.mark.ui
def test_place_bet_away(page):
    # --- Arrange ---
    home = HomePage(page)
    home.open()

    # Select next UPCOMING match
    match_id = home.select_next_upcoming_match()
    card = home.get_card_by_id(match_id)

    # --- Act ---
    # Click AWAY odds
    home.click_away_odds(card)

    betslip = BetSlipPage(page)
    betslip.wait_until_visible()

    stake = 10.0
    betslip.enter_bet_amount(str(stake))

    # --- Assert ---
    assert betslip.get_match_winner() == "Away"

    odds = betslip.get_odds_multiplier()
    payout = betslip.get_payout_value()
    expected = betslip.calculate_expected_payout(stake, odds)

    assert payout == expected