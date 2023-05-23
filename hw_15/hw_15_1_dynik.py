class Auto:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("Авто рухається.")

    def stop(self):
        print("Авто зупинено.")

    def get_details(self):
        return f"Марка: {self.make}, Модель: {self.model}, Рік: {self.year}"


auto1 = Auto("Toyota", "Camry", 2022)
print(auto1.get_details())

auto2 = Auto("Honda", "Civic", 2021)
print(auto2.get_details())

auto1.drive()
auto2.stop()
