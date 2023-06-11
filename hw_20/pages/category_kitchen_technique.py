from hw_20.pages.basepage import BasePage
from hw_20.pages.electric_grill_page import ElectricGrillPage
from hw_20.core.locator import Locator
from hw_20.locators.appliances_locators import AppliancesLocators


class CategoryPickPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__for_kitchen_technique_locator = AppliancesLocators().for_kitchen_technique_locator

    def choose_kitchen_technique_category(self):
        self._click(self.__for_kitchen_technique_locator)
        return ElectricGrillPage(self.driver)
