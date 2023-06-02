from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
import pytest
# from pages.dashboard import Dashboard
from hw_19.pages.dashboard import Dashboard
from hw_19.pages.feedbackpage import Feedback


@pytest.fixture(scope='session')
def driver():
    driver = Chrome('hw_19/drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://rst.ua/ukr/')

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)


@pytest.fixture
def feedback(driver):
    yield Feedback(driver)
