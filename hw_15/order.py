from pizza import Pizza
from pasta import Pasta
from risotto import Risotto


class OrderPart:
    def __init__(self):
        self.order = []

    def add_dish(self, dish):
        self.order.append(dish)

    def remove_dish(self, dish):
        self.order.remove(dish)

    def get_total_price(self):
        total_price = sum(dish.get_price() for dish in self.order)
        return total_price

    def get_dish(self, dish_type):
        if dish_type == "Risotto":
            return Risotto('Vialone Nano', 125, 'Semifino Vialone Nano rice')
        elif dish_type == "Pasta":
            return Pasta('Bucatini pasta', 200, ['Bucatini', 'pancetta', 'yellow onion'])
        elif dish_type == "Pizza":
            return Pizza('Neapolitan pizza', 180, ['Pizza dough', 'Easy Pizza Sauce', 'fresh mozzarella cheese'])
        else:
            raise ValueError("Invalid dish type")


order_part = OrderPart()
dish1 = order_part.get_dish("Risotto")
dish2 = order_part.get_dish("Pizza")

print(dish1.get_description())
print(dish2.get_description())
