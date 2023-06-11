from selenium.webdriver import Chrome
import pytest

from hw_20.pages.mainpage import MainPage


@pytest.fixture(scope='session')
def driver():
    driver = Chrome('hw_20/drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://allo.ua/')

    yield driver

    driver.quit()


@pytest.fixture
def mainpage(driver):
    yield MainPage(driver)
