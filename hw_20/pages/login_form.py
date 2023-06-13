from hw_20.pages.basepage import BasePage
from hw_20.locators.login_form_locators import LoginFormLocators
from hw_20.core.locator import Locator


class LoginForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__login_and_pass_locator = LoginFormLocators().login_and_pass_locator
        self.__email_input_locator = LoginFormLocators().email_input_locator
        self.__password_locator = LoginFormLocators().password_locator
        self.__enter_button_locator = LoginFormLocators().enter_button_locator

    def click_on_login_and_pass(self):
        self._click(self.__login_and_pass_locator)

    def send_email(self):
        email = self._wait_until_element_appears(self.__email_input_locator)
        email.send_keys('necid43225@pyadu.com')

    def send_pass(self):
        passw = self._wait_until_element_appears(self.__password_locator)
        passw.send_keys('Kola007')

    def click_enter_button(self):
        self._click(self.__enter_button_locator)

    def login(self):
        self.click_on_login_and_pass()
        self.send_email()
        self.send_pass()
        self.click_enter_button()
