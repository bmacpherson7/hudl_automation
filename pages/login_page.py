from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    # Test Data
    LOGIN_TITLE = 'Log In'
    FORGOT_PASSWORD_TITLE = 'Reset Password'
    CREATE_ACCOUNT_TITLE = 'Create Account'

    MISSING_EMAIL_ERROR = 'Enter an email address'
    ILLEGAL_EMAIL_ERROR = 'Enter a valid email.'
    INVALID_EMAIL_ERROR = 'Incorrect username or password.'
    MISSING_PASSWORD_ERROR = 'Enter your password.'
    INVALID_PASSWORD_ERROR = 'Your email or password is incorrect. Try again.'

    # Locators
    EMAIL_TEXTBOX = (By.ID, 'username')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button[name="action"]')
    PASSWORD_TEXTBOX = (By.ID, 'password')
    ERROR_MESSAGE = (By.CLASS_NAME, '_prompt-box-outer')
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, 'Create Account')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Forgot Password')

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.hudl.com/login'

    def enter_email(self, email):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.EMAIL_TEXTBOX)).send_keys(email)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def login(self, email, password):
        self.enter_email(email)
        self.driver.find_element(*self.PASSWORD_TEXTBOX).send_keys(password)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_login(self):
        self.find_element(*self.CONTINUE_BUTTON).click()

    def click_create_account(self):
        self.find_element(*self.CREATE_ACCOUNT_LINK).click()
    
    def click_forgot_password(self):
        self.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def get_error_text(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
