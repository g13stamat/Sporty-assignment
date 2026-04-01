import pytest
from helpers.date_utils import is_future_match, is_bettable

@pytest.mark.api
@pytest.mark.parametrize("outcome", ["home", "draw", "away"])
def test_place_bet(api, outcome):
    # --- Arrange ---
    # Fetch matches and filter to future, bettable ones
    matches = api.get("/matches").json()
    print(f"[DEBUG] Total matches returned: {len(matches)}")

    bettable_matches = [
        m for m in matches
        if is_future_match(m) and is_bettable(m)
    ]
    assert bettable_matches, "No bettable matches available"

    match = bettable_matches[0]
    match_id = match["id"]
    odds = match["odds"]
    stake = 10.0

    print(f"[DEBUG] Placing bet on match: {match_id}")
    print(f"[DEBUG] Outcome: {outcome.upper()}, Stake: {stake}, Odds: {odds[outcome]}")

    # Build payload using valid selection and stake
    payload = {
        "matchId": match_id,
        "selection": outcome.upper(),
        "stake": stake,
    }
    print(f"[DEBUG] Payload: {payload}")

    # --- Act ---
    response = api.post("/place-bet", json=payload)
    print(f"[DEBUG] Response {response.status_code}: {response.text}")

    # --- Assert ---
    # Successful bet placement must return 200 or 201
    assert response.status_code in (200, 201), "Bet placement should succeed"

    bet = response.json()

    # Expected payout = stake * selected odds
    expected_payout = round(odds[outcome] * stake, 2)
    print(f"[DEBUG] Expected payout: {expected_payout}")

    assert bet["payout"] == expected_payout, (
        f"Payout mismatch: expected {expected_payout}, got {bet['payout']}"
    )