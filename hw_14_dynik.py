class Train:
    def __init__(self):
        self.name = None
        self.number = None
        self.train_type = None
        self.num_train_cars = None
        self.train_car = []
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        self.speed -= speed_decrease

    def add_train_car(self, train_car):
        self.train_car.append(train_car)

    def __str__(self):
        return f"Train {self.number}, type: {self.train_type}, number of train cars: {self.num_train_cars}, " \
               f"speed: {self.speed} km/h"

    def __len__(self):
        return len(self.train_car) - 1

    # Need to implement
    def stop_at_the_station(self, station_name, enter_passengers, exit_passengers):
        print(f'Train {self.name} stopped at the {station_name}')


class TrainCar:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.passengers = []

    def get_number(self):
        return self.number

    def get_capacity(self):
        return self.capacity

    def set_number(self, new_number):
        self.number = new_number

    def set_capacity(self, new_capacity):
        self.capacity = new_capacity

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
        else:
            print('The train car is full')

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
        else:
            print(f'We can\'t remove {passenger}')

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        passenger_info = []
        for passenger in self.passengers:
            info = f'"name": "{passenger.name}", "destination": "{passenger.destination}", ' \
                   f'"place in train": "{passenger.place_in_train}"'
            passenger_info.append(info)
        return f'{passenger_info}'


class Lokomotive(TrainCar):
    pass


class Passenger:
    def __init__(self, name, destination, place_in_train):
        self.name = name
        self.destination = destination
        self.place_in_train = place_in_train


train1 = Train()
train1.add_train_car(Lokomotive(1, 2))
train1.add_train_car(TrainCar(2, 3))
train1.add_train_car(TrainCar(3, 1))
train1.add_train_car(TrainCar(4, 5))


train_car1 = TrainCar(1, 80)
train_car1.add_passenger(Passenger('Andre Onana', 'Milan', 90))
train_car1.add_passenger(Passenger('Romelu Lukaku', 'Milan', 12))
train_car1.add_passenger(Passenger('Nikolo Barella', 'Milan', 5))
print(train_car1)

