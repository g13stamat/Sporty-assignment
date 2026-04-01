import pytest
from pages.home_page import HomePage
from pages.betslip_page import BetSlipPage

@pytest.mark.ui
def test_ui_stake_reset_when_selecting_new_match(page):
    # --- Arrange ---
    home = HomePage(page)
    home.open()

    # Select first UPCOMING match and open betslip
    first_match_id = home.select_next_upcoming_match()
    first_card = home.get_card_by_id(first_match_id)
    home.click_home_odds(first_card)

    betslip = BetSlipPage(page)
    betslip.wait_until_visible()

    # Enter initial stake
    initial_stake = "5.00"
    betslip.enter_bet_amount(initial_stake)

    # Verify stake is set
    assert betslip.get_bet_amount() == float(initial_stake)

    # --- Act ---
    # Select a different match
    second_match_id = home.select_next_upcoming_match()
    assert second_match_id != first_match_id

    second_card = home.get_card_by_id(second_match_id)
    home.click_home_odds(second_card)

    # --- Assert ---
    # BetSlip should reset after selecting a new match
    assert betslip.get_bet_amount() == 0.0
    assert betslip.get_payout_value() == 0.0