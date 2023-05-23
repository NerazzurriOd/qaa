from dish import Dish


class Pasta(Dish):
    def __init__(self, name, price, sauce):
        super().__init__(name, price)
        self.sauce = sauce

    def get_description(self):
        return "Pasta"
