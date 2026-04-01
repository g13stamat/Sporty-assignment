📄 TEST PLAN (5–6 PRIORITIZED SCENARIOS)
File: test_plan.md

### 1. Overview
This test plan focuses on validating the core sportsbook functionality for the “Sports Betting QA” assignment.
The goal is to ensure that the most critical user journeys and business rules behave correctly.

### 2. Scope
UI tests (Playwright): Here we should cover the UI responds to the user actions and different possible journeys. 

API tests (GET /matches, GET /balance): Here we cover how the system behaves on different data inputs. 

Manual exploratory tests: Here we should cover both UI and API cases that live outside the documented flows.

Functional validation of betslip, odds, payout, and bet placement


### 3. Prioritized Test Scenarios
⭐ P1 — Place a bet on an upcoming match - core flow that should be part of the regression suite. (automated UI)

Objective: Ensure a user can select odds, enter a stake, and place a bet.

Expected: Betslip opens, payout is calculated, bet is accepted.

Covered by: test_ui_place_bet_user_journey.py

Result -> FAIL

BugID: 2 


⭐ P1 — Betslip calculates payout correctly - core flow that should be part of the regression suite. (automated UI)

Objective: Validate payout = stake × odds.

Expected: UI payout matches expected calculation.

Covered by: test_ui_place_bet_home.py,
            test_ui_place_bet_draw.py,
            test_ui_place_bet_away.py,
            test_ui_stake_denominations.py

Result -> PASS 


⭐ P1 — Selecting a new match resets the betslip - core flow that should be part of the regression suite. (automated UI)

Objective: Ensure switching matches clears stake and payout.

Expected: Stake resets to 0.00, payout resets to 0.00.

Covered by: test_ui_stake_reset_when_selecting_new_match.py

Result -> PASS


⭐ P1 — User cannot place a bet with insufficient balance - critical requirement (Exploratory for now) 

Objective: Validate business rule enforcement.

Expected: PLACE BET disabled, warning shown.

Result -> FAIL

BugID: 3 


⭐ P1 — User cannot place a bet on a PAST match - normally the UI should be filtering out expired matches. (Exploratory for now) 

Objective: Ensure sportsbook prevents invalid betting.

Expected: Odds disabled, betslip should not open.

Result -> FAIL

BugID: 1


⭐ P1 — User can bet on home team, away team or match draw - core flow that should be part of the regression suite. (automated UI)

Objective: Validate Home / Draw / Away odds selection.

Expected: Betslip reflects correct market and odds.

Covered by: test_ui_place_bet_home.py,
            test_ui_place_bet_draw.py,
            test_ui_place_bet_away.py,

Result -> PASS


⭐ P1 — User can bet a stake of 1 up to 100 euros - core flow that should be part of the regression suite. (automated UI)

Objective: Validate Home / Draw / Away odds selection.

Expected: Betslip reflects correct market and odds.

Covered by: test_ui_stake_denominations.py

Result -> PASS


⭐ P1 — Testing invalid stakes (-1, -0.1, 1.111, 100.1)  - core flow that should be part of the regression suite. (automated API)

Objective: Validate Home / Draw / Away odds selection.

Expected: Response reflects incorect stake.

Covered by: test_api_invalid_stakes.py

Result -> FAIL

BugID: 3,4,5


⭐ P1 — Place bet via API call - core flow that should be part of the regression suite. (automated API)

Objective: Validate placing bet response.

Expected: Response reflects correct market and odds.

Covered by: test_api_place_bet.py

Result -> PASS


⭐ P1 — Testing invalid outcome selection ("home", "invalid", "", 123, etc)  - core flow that should be part of the regression suite. (automated API)

Objective: Validate Home / Draw / Away selection.

Expected: Response reflects incorrect selection.

Covered by: test_api_invalid_selection.py

Result -> PASS


⭐ P1 — Getting all available matches via API call  - core flow that should be part of the regression suite. (automated API)

Objective: Validate Home / Draw / Away selection.

Expected: Response retrieves the matches.

Covered by: test_api_get_matches.py

Result -> PASS


### 4. Risk Management

This assignment focuses on validating critical sportsbook functionality under realistic constraints.  

The following risks were identified and mitigated through targeted test design:

### 🔥 High‑Impact Risks (P1)

** Incorrect payout calculation**  

- *Risk:* Users receive wrong payout values, leading to financial loss or mistrust.  

- *Mitigation:* Automated UI tests validate payout = stake × odds for multiple scenarios.

** Ability to place invalid bets (negative stake, past matches)**  

- *Risk:* Business logic violations allow bets that should be rejected.  

- *Mitigation:* API tests enforce validation rules; exploratory UI and API tests revealed real defects.

** Betslip not updating correctly**  

- *Risk:* Users place bets with stale odds or mismatched selections.  

- *Mitigation:* UI tests verify odds selection, betslip reset, and modal accuracy.

### ⚠️ Medium Risks (P2)

** UI inconsistencies across browsers**  

- *Risk:* Different rendering engines (Chromium, Firefox, WebKit) may behave differently.  

- *Mitigation:* Suite executed across all three browsers using Playwright’s cross‑browser engine.

** Incorrect handling of insufficient balance**  

- *Risk:* Users may be allowed to place bets they cannot afford.  

- *Mitigation:* UI tests validate button state and warning messages.

### 🧊 Low Risks (P3)

** Non‑functional issues (performance, load, concurrency)**  

- *Risk:* High traffic or simultaneous users could degrade experience.  

- *Mitigation:* Out of scope for this assignment; noted for future testing.

---

### 5. Test Data & Environment Assumptions

- A single test user is provided with an initial balance (expected: €100).

- Match list is controlled by the backend and cannot be manipulated by the tester.

- Odds and match availability may change between runs.

- No mechanism exists to reset user balance between tests.

- No stubbing or mocking is available; all tests run against live backend responses.

- Time-dependent scenarios (e.g., past matches) cannot be controlled or simulated.
