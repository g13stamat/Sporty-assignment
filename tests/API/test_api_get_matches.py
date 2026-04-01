import pytest

@pytest.mark.api
def test_get_matches(api):
    # --- Arrange & Act ---
    # Call the matches endpoint
    response = api.get("/matches")
    print(f"[DEBUG] GET /matches → {response.status_code}")

    # --- Assert: Basic response validation ---
    assert response.status_code == 200, "Expected 200 OK from /matches"

    data = response.json()
    print(f"[DEBUG] Number of matches returned: {len(data)}")

    # The endpoint must return a non-empty list of matches
    assert isinstance(data, list), "Response must be a list"
    assert len(data) > 0, "Expected at least one match in the response"

    # --- Assert: Validate structure of the first match ---
    match = data[0]
    print(f"[DEBUG] First match: {match}")

    required_fields = [
        "id",
        "homeTeam",
        "awayTeam",
        "competition",
        "kickoffDate",
        "odds",
    ]

    # Ensure all required fields exist
    for field in required_fields:
        assert field in match, f"Missing field in match object: {field}"

    # --- Assert: Validate odds structure ---
    odds = match["odds"]
    assert isinstance(odds, dict), "Odds must be a dictionary"

    for key in ["home", "draw", "away"]:
        assert key in odds, f"Missing odds key: {key}"
        assert isinstance(odds[key], (int, float)), f"Odds for {key} must be numeric"
        assert odds[key] > 1.0, f"Odds for {key} must be > 1.0"

    print("[DEBUG] Odds structure validated successfully")