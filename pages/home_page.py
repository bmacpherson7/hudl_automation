from pages.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    # Test Data
    HOME_TITLE = 'Home'

    # Locators
    USER_AVATAR = (By.CSS_SELECTOR, 'div.hui-globalusermenu')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[data-qa-id="webnav-usermenu-logout"]')

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def click_logout(self):
        self.hover(*self.USER_AVATAR);
        self.wait_then_find(*self.LOGOUT_BUTTON).click()
