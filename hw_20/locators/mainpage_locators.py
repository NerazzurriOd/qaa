from hw_20.core.locator import Locator


class MainPageLocators:
    def __init__(self):
        self.__nav_bar_locator = Locator('xpath', '//div[@class="mh-catalog-btn"]/div[@class="ct-button"]')
        self.__title_locator = Locator('xpath', '//head/title')
        self.__footer_text_locator = Locator('xpath', '//p[@class="footer-copyright__text"]')
        self.__sellers_menu_locator = Locator('xpath',
                                              '//div[@class="mh-button__wrap"]/a[contains(text(), "Покупцям")]')
        self.__logo_locator = Locator('xpath', '//div[@class="mh__sr"]/a[@class="v-logo"]')

    @property
    def nav_bar_locator(self):
        return self.__nav_bar_locator

    @property
    def title_locator(self):
        return self.__title_locator

    @property
    def footer_text_locator(self):
        return self.__footer_text_locator

    @property
    def sellers_menu_locator(self):
        return self.__sellers_menu_locator

    @property
    def logo_locator(self):
        return self.__logo_locator
