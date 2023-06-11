from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw_20.core.locator import Locator


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._web_driver_wait = WebDriverWait(self.driver, 2)

    def _wait_until_element_appears(self, locator: Locator):
        return self._web_driver_wait.until(EC.presence_of_element_located(locator.to_tuple()))

    def _return_title(self, title):
        return self._web_driver_wait.until(EC.title_is(title))

    def _link_is(self, url):
        return self._web_driver_wait.until(EC.url_to_be(url))

    def _click(self, locator: Locator):
        self._wait_until_element_appears(locator).click()
