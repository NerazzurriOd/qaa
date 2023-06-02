from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._web_driver_wait = WebDriverWait(self.driver, 5)

    def _wait_until_element_appears(self, locator):
        return self._web_driver_wait.until(EC.presence_of_element_located(locator))

    def _wait_button_to_be_clickable(self, locator):

        return self._web_driver_wait.until(EC.element_to_be_clickable(locator))

    def _wait_text_to_be_presented(self, locator, text):
        return self._web_driver_wait.until(EC.text_to_be_present_in_element(locator, text))

