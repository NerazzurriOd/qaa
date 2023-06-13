from hw_20.pages.basepage import BasePage


class LocalStorage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_item(self, key):
        return self.driver.execute_script(f'return window.localStorage.getItem("{key}");')

    def set_item(self, key, value):
        self.driver.execute_script(f'window.localStorage.setItem("{key}, "{value}");')

    def remove_item(self, key):
        self.driver.execute_script(f'window.localStorage.removeItem("{key}");')
