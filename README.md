# Sporty Assignment – Automated Testing Suite  
Author: Giorgos  
Role: Senior QA Engineer & Scrum Master  

This repository contains a complete automated testing solution for the Sporty assignment, covering both **API** and **UI** flows.  
The suite is built with **pytest**, **Playwright**, and **requests**, and is designed to be stable, maintainable, and easy for reviewers to execute.

---

## 📌 Project Overview

The test suite validates:

### ✅ API Layer
- Stake validation rules  
- Error handling  
- Business logic constraints  
- Boundary values (negative, decimal, invalid inputs)

### ✅ UI Layer (Playwright)
- User journey for placing a bet  
- Odds display and payout calculation  
- Modal validation  
- Cross‑browser compatibility (Chromium, Firefox, WebKit)

### 📁 Artifacts
- **Screenshots on failure** (saved under `/screenshots`)  
- **Console logs** (pytest output)  
- **Bug report** (`bug_report.md`)  
- **Test plan** (`test_plan.md`)  

---

## 🧱 Project Structure

sporty-assignment/
│
├── helpers/
│   └── api_client.py
│
├── tests/
│   ├── API/
│   │   └── test_api_invalid_stakes.py
│   └── UI/
│       └── test_ui_place_bet_user_journey.py
│
├── utils/
│
├── screenshots/          # auto‑generated on failures
│
├── conftest.py           # fixtures + screenshot hook
├── pytest.ini            # markers only
├── requirements.txt
├── README.md
├── test_plan.md
└── bug_report.md


---

## 🚀 How to Set Up the Environment

### 1. Create & activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

2. Install dependencies
bash
pip install -r requirements.txt
3. Install Playwright browsers
bash
playwright install

▶️ How to Run the Tests
Run the full suite (API + UI)
bash
pytest
Run only UI tests
bash
pytest -m ui --browser chromium --headed
Run only API tests
bash
pytest -m api

🌐 Cross‑Browser Execution (UI)
The suite supports Chromium, Firefox, and WebKit out of the box.

Run all browsers:

bash
pytest --browser all --headed
Run a specific browser:

bash
pytest --browser chromium --headed
pytest --browser firefox --headed
pytest --browser webkit --headed
No code changes required — Playwright handles browser selection automatically.

📸 Screenshots on Failure
Whenever a UI test fails, a screenshot is automatically saved to:

Code
/screenshots/<test_name>_<timestamp>.png
This works without any HTML report plugins, ensuring stability and reproducibility.

🧪 Test Design & Strategy
See test_plan.md for:

Scope & objectives

Test scenarios

Risk analysis

Coverage strategy

Browser matrix

API validation approach

🐞 Bug Reporting
All identified defects are documented in bug_report.md, including:

Steps to reproduce

Expected vs actual behavior

Severity

Impact on user journey


🧩 Notes for the Reviewer
The suite is intentionally plugin‑light to avoid cross‑platform issues.

Screenshots are saved locally instead of embedded in HTML reports for maximum stability.

Multi‑browser execution is fully supported and tested.

The framework is modular and easy to extend (new endpoints, new UI flows, etc.).

