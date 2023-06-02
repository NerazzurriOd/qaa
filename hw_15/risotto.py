from dish import Dish


class Risotto(Dish):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients
        name = 'Risotto'

    def get_description(self):
        return "Risotto"
