from hw_19.pages.basepage import BasePage


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__nav_bar_locator = ('xpath', '//i[@class="icon-menu"][1]')

    def click_on_navbar(self):
        element = self._wait_until_element_appears(self.__nav_bar_locator)
        element.click()

    def choose_subcategory(self, name):
        locator = ('xpath', f'//b[contains(text(), "{name}")]')
        element = self._wait_until_element_appears(locator)
        element.click()
