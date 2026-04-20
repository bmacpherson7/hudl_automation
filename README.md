# Hudl Automation

A lightweight Selenium + pytest automation project for Hudl login flows.

## Overview

This repository contains a simple UI automation suite using pytest, Selenium WebDriver, and the Page Object Model. It includes login path tests for both valid and invalid credentials, plus negative validation scenarios.

## Repo Structure

- `conftest.py` — pytest fixtures, WebDriver setup, browser CLI options, and environment variable loading
- `requirements.txt` — Python dependencies
- `pages/` — Page Object Model classes for `BasePage`, `LoginPage`, and `HomePage`
- `tests/` — pytest test cases for login flows
- `.env.example` — example environment variables for local test credentials
- `.gitignore` — excludes local environment files, caches, IDE settings, and other unnecessary artifacts

## Prerequisites

- Python 3.11+ (or compatible Python 3.x)
- Git
- A supported browser: Chrome or Firefox

## Setup

1. Clone the repository:

```bash
git clone https://github.com/bmacpherson7/hudl_automation.git
cd hudl_automation
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure your test credentials:

```bash
cp .env.example .env
```

Edit `.env` and set the following values:

```env
TEST_USER_EMAIL=your_test_email@example.com
TEST_USER_PASSWORD=YourSecurePassword123!
```

## Running Tests

Run the suite with Chrome by default:

```bash
pytest
```

Run tests in Firefox:

```bash
pytest --browser firefox
```

Run headless tests:

```bash
pytest --headless
```

Run Firefox headless:

```bash
pytest --browser firefox --headless
```

## Environment Variables

The suite reads credentials from `.env` via `python-dotenv`.

- `TEST_USER_EMAIL` — test account email
- `TEST_USER_PASSWORD` — test account password

If these values are not set, fallback defaults are used but may not log in successfully.

## Notes

- `webdriver-manager` automatically downloads and manages browser driver binaries.
- Tests currently focus on login page validation and logout flow.
- The page objects are implemented in `pages/login_page.py` and `pages/home_page.py`.

## Recommended Workflow

1. Update `.env` with valid Hudl test credentials.
2. Run `pytest --browser chrome --headless` for CI-style execution.
3. Inspect failures in the terminal and update page locators if UI changes.

---

If you want, I can also add a `pytest.ini` or GitHub Actions workflow for CI execution.