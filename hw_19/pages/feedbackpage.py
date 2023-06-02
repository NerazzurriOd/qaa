from hw_19.pages.basepage import BasePage
from hw_19.pages.dashboard import Dashboard


class Feedback(Dashboard):
    def __init__(self, driver):
        super().__init__(driver)
        self.__feedback_button_locator = ('xpath', '//li/a[@href="//rst.ua/ukr/help/feedback.html"]')
        self.__text_area_locator = ('xpath', '//textarea[@class="form-control"]')
        self.__name_input_locator = ('xpath', '//input[@id="email"]')
        self.__send_button_locator = ('xpath', '//button[contains(text(), "Відправити")]')
        self.__success_message_locator = ('xpath', '//div[contains(text(), "Дякуємо за відгук")]')

    def open_feedback_page(self):
        self.click_on_navbar()
        element = self._wait_until_element_appears(self.__feedback_button_locator)
        element.click()

    def find_text_area(self):
        return self._wait_until_element_appears(self.__text_area_locator)

    def write_feedback_text(self, text):
        element = self._wait_until_element_appears(self.__text_area_locator)
        element.send_keys(text)

    def find_name_input(self):
        return self.__name_input_locator

    def enter_name(self, name):
        element = self._wait_until_element_appears(self.__name_input_locator)
        element.send_keys(name)

    def find_send_button(self):
        return self._wait_button_to_be_clickable(self.__send_button_locator)

    def success_message(self, text):
        return self._wait_text_to_be_presented(self.__success_message_locator, f'{text}')
