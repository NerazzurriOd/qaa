from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def move(self):
        """Should implement method move"""

    @abstractmethod
    def stop(self):
        """Should implement method stop"""

    @abstractmethod
    def get_speed(self):
        """Should implement method get speed"""


class Car(Transport):
    def __init__(self, brand, model, max_speed):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.speed = 0

    def move(self):
        print(f"{self.brand} {self.model} is moving")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} {self.model} stopped")

    def get_speed(self):
        self.speed = self.max_speed / 2
        return self.speed


class Truck(Car):
    def __init__(self, brand, model, max_speed, max_weight):
        super().__init__(brand, model, max_speed)
        self.max_weight = max_weight
        self.current_weight = 12000

    def load(self, weight):
        if weight + self.current_weight <= self.max_weight:
            self.current_weight += weight
            print(f"Loaded {weight} kg")
        else:
            print("Cannot load. Exceeds max weight")

    def move(self):
        print(f"{self.brand} {self.model} is moving")

    def stop(self):
        print(f"{self.brand} {self.model} stopped")


my_car = Car('Toyota', 'Corolla', 160)
my_car.move()
my_car.stop()


my_truck = Truck('Man', 'HZ', 120, 30000)
my_truck.load(15000)
