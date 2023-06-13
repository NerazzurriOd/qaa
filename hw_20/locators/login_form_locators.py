from hw_20.core.locator import Locator


class LoginFormLocators:
    def __init__(self):
        self.__login_and_pass_locator = Locator('xpath', '//div[@class="auth__enter-password"]/button')
        self.__email_input_locator = Locator('xpath', '//div[@class="a-input__container"]/input[@name="phoneEmail"]')
        self.__password_locator = Locator('xpath', '//div[@class="a-input__container"]/input[@name="password"]')
        self.__enter_button_locator = Locator('xpath', '//span[@class="a-button__text"]')

    @property
    def login_and_pass_locator(self):
        return self.__login_and_pass_locator

    @property
    def email_input_locator(self):
        return self.__email_input_locator

    @property
    def password_locator(self):
        return self.__password_locator

    @property
    def enter_button_locator(self):
        return self.__enter_button_locator
