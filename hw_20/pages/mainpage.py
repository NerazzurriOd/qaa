from hw_20.pages.basepage import BasePage
from hw_20.pages.category_kitchen_technique import CategoryPickPage
from hw_20.core.locator import Locator
from hw_20.locators.mainpage_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__nav_bar_locator = MainPageLocators().nav_bar_locator
        self.__title_locator = MainPageLocators().title_locator
        self.__footer_text_locator = MainPageLocators().footer_text_locator
        self.__sellers_menu_locator = MainPageLocators().sellers_menu_locator
        self.__logo_locator = MainPageLocators().logo_locator

    def click_on_navbar(self):
        self._click(self.__nav_bar_locator)

    def choose_subcategory(self, name):
        self._click(Locator('xpath', f'//a[text()[normalize-space() = "{name}"]]'))
        return CategoryPickPage(self.driver)

    def find_footer(self):
        return self._wait_until_element_appears(self.__footer_text_locator)

    def choose_header_page(self, name):
        self._click(Locator('xpath', f'//div[@class="mh-links"]/a[contains(text(), "{name}")]'))

    def choose_sellers_menu(self):
        return self._wait_until_element_appears(self.__sellers_menu_locator)

    def choose_sellers_subpages(self, name):
        self.choose_sellers_menu().click()
        self._click(Locator('xpath', f'//div[@class="mh-button__dropdown"]/a[contains(text(), "{name}")]'))

    def check_link(self, url):
        return self._link_is(url)

    def find_logo(self):
        return self._wait_until_element_appears(self.__logo_locator)
