from hw_19.pages.basepage import BasePage


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__nav_bar_locator = ('xpath', '//i[@class="icon-menu"][1]')
        self.__h1_locator = ('xpath', '//h1[contains(text(), "Авто базар - Авторинок України.")]')
        self.__footer_locator = ('xpath', '//footer/small[@class="text-grey"]')
        self.__favorite_button_locator = ('xpath', '//a[@class="bstar"][1]')
        self.__count_added_cars_to_favorite_locator = ('xpath', '//a[@data-bs-toggle="modal"][1]/i[@class ="bstar-s"]'
                                                                '[contains(text(), "1")]')
        self.__notebook_locator = ('xpath', '//a[@id="bstar"]/b[contains(text(), "Мій блокнот")][1]')
        self.__delete_favorite_button_locator = ('xpath', '//a[@title="видалити з блокноту"]')
        self.__deleted_car_from_favorite_locator = ('xpath', '//a[@data-bs-toggle="modal"]/i[contains(text(), "0")]')

    def click_on_navbar(self):
        element = self._wait_until_element_appears(self.__nav_bar_locator)
        element.click()

    def choose_subcategory(self, name):
        locator = ('xpath', f'//b[contains(text(), "{name}")]')
        element = self._wait_until_element_appears(locator)
        element.click()

    def find_title(self):
        return self._wait_until_element_appears(self.__h1_locator)

    def find_footer(self):
        return self._wait_until_element_appears(self.__footer_locator)

    def add_car_to_favorite(self):
        element = self._wait_until_element_appears(self.__favorite_button_locator)
        element.click()

    def count_of_added_car_to_favorite(self):
        self._wait_until_element_appears(self.__count_added_cars_to_favorite_locator)

    def open_notebook(self):
        element = self._wait_until_element_appears(self.__notebook_locator)
        element.click()

    def delete_from_favorite(self):
        element = self._wait_until_element_appears(self.__delete_favorite_button_locator)
        element.click()

    def count_of_deleted_cars_from_favorite(self):
        return self._wait_until_element_appears(self.__deleted_car_from_favorite_locator)
