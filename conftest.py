import pytest
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

load_dotenv()

TEST_USER_EMAIL = os.getenv('TEST_USER_EMAIL', 'test@test.com')
TEST_USER_PASSWORD = os.getenv('TEST_USER_PASSWORD', 'ThisIsATestPassword123!')
TEST_USER_ILLEGAL_EMAIL = 'ooogaboogabooga'
TEST_USER_INVALID_EMAIL = 'asdf@asdf.cz'
TEST_USER_INVALID_PASSWORD = 'WrongPassword123!'

def pytest_addoption(parser):
    """Allows us to pass --browser from the command line."""
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser").lower()
    is_headless = request.config.getoption("--headless")
    
    if browser_name == "chrome":
        options = ChromeOptions()
        if is_headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if is_headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise pytest.UsageError("--browser must be chrome or firefox")

    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()