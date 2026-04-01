⭐ Critical Bugs
🐞 1. Betting is allowed on PAST matches
Severity: Critical
Area: UI + Backend
Type: Business Logic Violation

Steps to Reproduce
Open the sportsbook home page.

Scroll to a match that has already finished (past date/time).

Click on any odds (Home / Draw / Away).

Observe the betslip opening and allowing stake entry.

Attempt to place a bet.

Expected Result
Odds for past matches should be disabled.

Betslip should not open.

Backend should reject any attempt to place a bet on a past event.

Actual Result
Odds are enabled.

Betslip opens normally.

Bet can be placed successfully.

Impact
Enables fraudulent betting.

Violates core sportsbook rules.

High financial and reputational risk.

🐞 2. Payout calculation in confirmation modal is incorrect
Severity: Critical
Area: UI
Type: Calculation / Consistency Error

Steps to Reproduce
Select an upcoming match.

Click on any odds.

Enter a valid stake (e.g., 1.00).

Observe payout in the betslip (correct).

Click “Place Bet”.

Observe payout in the confirmation modal.

Expected Result
Payout in the modal should match the betslip calculation:
payout = stake × odds

Actual Result
Betslip shows correct payout (e.g., 2.35).

Confirmation modal shows incorrect payout (e.g., 2.00).

Impact
Users see inconsistent payout values.

Violates financial accuracy requirements.

High risk of user complaints and financial disputes.

🐞 3. Betting is allowed with NEGATIVE balance (API)
Severity: Critical
Area: API
Type: Validation Failure

Steps to Reproduce
Send a POST request to /place-bet with:

valid match

valid odds

valid stake

balance < 0

Observe the API response.

Expected Result
API should return 422 or 400 with validation error.

Bet should be rejected.

Actual Result
API returns 200 OK.

Bet is accepted despite negative balance.

Impact
Users can effectively “print money”.

Financial integrity is broken.

Critical backend validation flaw.

🐞 4. Balance currency changes to USD after placing a bet
Severity: Critical
Area: API
Type: Data Integrity Issue

Steps to Reproduce
Check initial balance (EUR).

Place a valid bet via API.

Retrieve balance again.

Expected Result
Currency should remain consistent (EUR).

Actual Result
Currency changes to USD after placing a bet.

Impact
Breaks financial reporting.

Affects revenue calculations, payouts, and accounting.

Indicates deeper data consistency issues.

⭐ Major Bugs
🐞 5. Test user balance does not reset between sessions
Severity: Major
Area: API
Type: Environment / Test Data Issue

Steps to Reproduce
Retrieve balance via /balance.

Place a bet via /place-bet.

Retrieve balance again.

Repeat multiple times.

Expected Result
Test user balance should reset per session or per test run.

Alternatively, a dedicated endpoint should exist to reset balance.

Actual Result
Balance decreases permanently with each bet.

No reset mechanism exists.

Impact
Blocks repeatable test execution.

Prevents stable automation.

Forces testers to rely on bug #3 (negative balance acceptance) to continue testing.