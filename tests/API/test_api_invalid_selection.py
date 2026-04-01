import pytest
from helpers.date_utils import is_future_match, is_bettable

@pytest.mark.api
@pytest.mark.parametrize(
    "invalid_selection",
    [
        "home",      # wrong case
        "invalid",   # not a valid option
        "",          # empty string
        None,        # null value
        123,         # wrong type
    ],
)
def test_place_bet_invalid_selection(api, invalid_selection):
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
    print(f"[DEBUG] Testing invalid selection '{invalid_selection}' on match: {match_id}")

    # Build payload with valid stake but invalid selection
    payload = {
        "matchId": match_id,
        "selection": invalid_selection,
        "stake": 10.0,
    }
    print(f"[DEBUG] Payload: {payload}")

    # --- Act ---
    response = api.post("/place-bet", json=payload)
    print(f"[DEBUG] Response {response.status_code}: {response.text}")

    # --- Assert ---
    # Spec: invalid selection MUST be rejected
    assert response.status_code == 422, "Invalid selection should return 422"

    body = response.json()

    # Error contract validation
    assert body["error"] == "invalid_selection"
    assert body["message"] == "Selection must be one of: HOME, DRAW, AWAY."