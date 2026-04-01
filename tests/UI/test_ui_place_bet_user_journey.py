import pytest
from helpers.formatting import to_float
from pages.home_page import HomePage
from pages.betslip_page import BetSlipPage
from pages.bet_popup_page import BetPopupPage

@pytest.mark.ui
def test_ui_place_bet_user_journey(page):
    # --- Arrange ---
    home = HomePage(page)
    home.open()

    # Select next UPCOMING match
    match_id = home.select_next_upcoming_match()
    card = home.get_card_by_id(match_id)

    # --- Act ---
    # Click HOME odds to open betslip
    home.click_home_odds(card)

    betslip = BetSlipPage(page)
    betslip.wait_until_visible()

    # Extract odds
    odds = betslip.get_odds_multiplier()

    # Enter stake
    stake_amount = "1.00"
    betslip.enter_bet_amount(stake_amount)

    # Validate payout calculation (known bug may appear)
    expected = betslip.calculate_expected_payout(to_float(stake_amount), odds)
    actual = betslip.get_payout_value()
    assert actual == expected

    # Place bet
    betslip.place_bet()

    # --- Assert ---
    # Validate popup
    popup = BetPopupPage(page)
    popup.wait_for_visible()

    assert "Successfully" in popup.get_title()
    assert popup.get_stake() == float(stake_amount)
    assert popup.get_odds() == odds

    # Validate payout inside popup
    popup.validate_payout(stake_amount)

    # Close popup
    popup.close()