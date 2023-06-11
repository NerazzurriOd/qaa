from hw_20.core.locator import Locator


class AppliancesLocators:
    def __init__(self):
        self.__for_kitchen_technique_locator = Locator('xpath', '//a[@title="Для кухні"]')

    @property
    def for_kitchen_technique_locator(self):
        return self.__for_kitchen_technique_locator
