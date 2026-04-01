import pytest
from helpers.date_utils import is_future_match, is_bettable

@pytest.mark.api
@pytest.mark.parametrize(
    "invalid_stake",
    [
        -1,       # BUG: backend incorrectly accepts this
        -0.11,    # BUG: backend incorrectly accepts this
        0.1,      # below minimum allowed (1.00)
        1.111,    # invalid precision
        100.1,    # above maximum allowed (100.00)  
        -100,    # use this iteration to recharge the tester's account if needed :)
    ],
)
def test_place_bet_invalid_stake(api, invalid_stake):
    # --- Arrange ---
    matches = api.get("/matches").json()
    print(f"[DEBUG] Total matches returned: {len(matches)}")

    # Filter to future matches with odds
    bettable_matches = [
        m for m in matches
        if is_future_match(m) and is_bettable(m)
    ]
    assert bettable_matches, "No bettable matches available"

    match = bettable_matches[0]
    match_id = match["id"]
    print(f"[DEBUG] Testing invalid stake '{invalid_stake}' on match: {match_id}")

    payload = {
        "matchId": match_id,
        "selection": "HOME",   # valid selection so only stake is tested
        "stake": invalid_stake,
    }
    print(f"[DEBUG] Payload: {payload}")

    # --- Act ---
    response = api.post("/place-bet", json=payload)
    print(f"[DEBUG] Response {response.status_code}: {response.text}")

    # --- Assert ---
    # According to the spec, ALL invalid stakes must return 422.
    # The backend currently violates this for negative values.
    assert response.status_code == 422, (
        f"Expected 422 for invalid stake '{invalid_stake}', "
        f"but got {response.status_code}. "
        "This indicates a backend validation bug."
    )

    body = response.json()

    # Error contract validation
    assert "error" in body, "Error field missing in invalid stake response"
    assert "Stake" in body.get("message", ""), "Error message must reference stake validation"