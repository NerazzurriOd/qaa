from selenium.webdriver import Chrome
import pytest

from hw_20.pages.mainpage import MainPage
from hw_20.pages.login_form import LoginForm
from hw_20.pages.category_kitchen_technique import CategoryPickPage


@pytest.fixture(scope='session')
def driver():
    driver = Chrome('hw_20/drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://allo.ua/odesa')

    yield driver

    driver.quit()


@pytest.fixture
def mainpage(driver):
    yield MainPage(driver)


@pytest.fixture
def login_form(driver):
    yield LoginForm(driver)


@pytest.fixture
def kitchen_technique(driver):
    yield CategoryPickPage(driver)
