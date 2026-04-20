from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    def __init__(self, driver, base_url = 'https://www.hudl.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 10

    def get_title(self):
        return self.driver.title
    
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def wait_then_find(self, *locator, timeout=None):
        to = timeout or self.timeout
        WebDriverWait(self.driver, to).until(EC.visibility_of_element_located(locator))
        return self.find_element(*locator)

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_url(self):
        return self.driver.current_url

    def load(self):
        self.driver.get(self.url)
