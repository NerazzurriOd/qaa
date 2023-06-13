from hw_20.pages.basepage import BasePage


class Cookies(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cookie(self, name):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == name:
                return cookie['value']
        return None

    def set_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()
