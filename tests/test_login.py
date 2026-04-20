from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.home_page import HomePage
from conftest import (
    TEST_USER_EMAIL,
    TEST_USER_PASSWORD,
    TEST_USER_INVALID_EMAIL,
    TEST_USER_INVALID_PASSWORD,
    TEST_USER_ILLEGAL_EMAIL
)

def test_login_page_loads(driver):
    """Simple check to ensure the page loads correctly."""
    login_page = LoginPage(driver)
    login_page.load()
    assert login_page.LOGIN_TITLE in driver.title, 'Login page should have "Log In" in the title'

# Positive Test Cases

def test_login_happy_path(driver):
    """Verifies that a user can log in with valid credentials."""
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    
    login_page.load()
    login_page.login(TEST_USER_EMAIL, TEST_USER_PASSWORD)

    home_page.wait_then_find(*home_page.USER_AVATAR), 'Should see user avatar on home page after login' 
    assert home_page.HOME_TITLE in home_page.get_title(), 'Should see Home in the title after successful login'
    home_page.click_logout()

    assert home_page.HOME_TITLE not in home_page.get_title(), 'Should be logged out and not see Home in the title'

# Negative Test Cases

def test_login_without_email(driver):
    """Verifies that an error message appears when trying to log in without entering an email."""
    login_page = LoginPage(driver)
    
    login_page.load()
    login_page.click_login()
    
    error_text = login_page.get_error_text()
    assert login_page.MISSING_EMAIL_ERROR in error_text, 'Should display error for missing email'

def test_login_with_illegal_email(driver):
    """Verifies that an error message appears when trying to log in with an improperly formatted email."""
    login_page = LoginPage(driver)
    
    login_page.load()
    login_page.enter_email(TEST_USER_ILLEGAL_EMAIL)
    
    error_text = login_page.get_error_text()
    assert login_page.ILLEGAL_EMAIL_ERROR in error_text, 'Should display error for illegal email format'

def test_login_with_invalid_credentials(driver):
    """Verifies that an error message appears with invalid credentials."""
    login_page = LoginPage(driver)
    
    login_page.load()
    login_page.login(TEST_USER_INVALID_EMAIL, TEST_USER_INVALID_PASSWORD)
    
    error_text = login_page.get_error_text()
    assert login_page.INVALID_EMAIL_ERROR in error_text, 'Should display error for invalid email'

def test_login_with_invalid_password(driver):
    """Verifies that an error message appears with valid email, but invalid password."""
    login_page = LoginPage(driver)
    
    login_page.load()
    login_page.login(TEST_USER_EMAIL, TEST_USER_INVALID_PASSWORD)
    
    error_text = login_page.get_error_text()
    assert login_page.INVALID_PASSWORD_ERROR in error_text, 'Should display error for invalid password'


def test_login_without_password(driver):
    """Verifies that an error message appears when trying to log in without entering a password."""
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login(TEST_USER_EMAIL, '')

    error_text = login_page.get_error_text()
    assert login_page.MISSING_PASSWORD_ERROR in error_text, 'Should display error for missing password'

# Navigation Test Cases

def test_navigate_to_create_account(driver):
    """Verifies that the user can navigate to the Create Account page from the login page."""
    login_page = LoginPage(driver)

    login_page.load()
    login_page.click_create_account()

    assert login_page.CREATE_ACCOUNT_TITLE in login_page.get_title(), 'Should navigate to Create Account page'

def test_navigate_to_forgot_password(driver):
    """Verifies that the user can navigate to the Forgot Password page from the login page."""
    login_page = LoginPage(driver)

    login_page.load()
    login_page.enter_email(TEST_USER_INVALID_EMAIL)  # Need to enter email to reveal forgot password link
    login_page.click_forgot_password()

    assert login_page.FORGOT_PASSWORD_TITLE in login_page.get_title(), 'Should navigate to Forgot Password page'
