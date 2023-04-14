class Bird:
    def __init__(self, kind: str, color: str, size: int, location: str, gender: str, can_talk: bool):
        self.kind = kind
        self.color = color
        self.size = size
        self.location = location
        self.gender = gender
        self.can_talk = can_talk

    def fly(self):
        print(f'{self.kind} is flying now to {self.location}!')

    def change_location(self, new_location):
        self.location = new_location

    @staticmethod
    def is_adult(age):
        if age > 18:
            print('Old bird')
        elif 10 <= age >= 18:
            print('Middle age bird')
        else:
            print('Young bird')


pigeon = Bird('Pigeon', 'black', 10, 'Europe', 'man', False)
print(pigeon.gender)
pigeon.fly()
pigeon.change_location('USA')
pigeon.fly()
Bird.is_adult(18)
parrot = Bird('Parrot', 'red-yellow', 6, 'Ukraine', 'women', True)
print(parrot.color)


# Task 2
class DataArt:

    count_of_offices = 0

    def __init__(self, location: str, clients: str, number_of_employers: int, work_from_home: bool):
        self.location = location
        self.clients = clients
        self.number_of_employers = number_of_employers
        self.work_from_home = work_from_home
        DataArt.count_of_offices += 1

    @classmethod
    def get_company_offices(cls, text_file):  # Can implement get offices from some file in future
        location, clients, number_of_employers, work_from_home = text_file.split(',')
        return cls(location, clients, number_of_employers, work_from_home)

    @classmethod
    def get_count_of_offices(cls):
        return DataArt.count_of_offices


print(DataArt.get_count_of_offices())
odesa_office = DataArt('Odesa', 'Medical', 350, True)
print(DataArt.get_count_of_offices())
kyiv_office = DataArt.get_company_offices('Kyiv, Gaming, 500, True')
print(kyiv_office.clients)
print(DataArt.get_count_of_offices())
