from abc import ABC, abstractmethod


class Dish(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    @abstractmethod
    def get_description(self):
        pass
