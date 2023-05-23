from dish import Dish


class Pizza(Dish):
    def __init__(self, name, price, toppings):
        super().__init__(name, price)
        self.toppings = toppings

    def get_description(self):
        return "Pizza"
