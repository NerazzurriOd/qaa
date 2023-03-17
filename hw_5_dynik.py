import random
from string import ascii_lowercase
from random import randint, sample, choice
from functools import reduce

# Task 1
print('Task 1')


def entered_sides() -> float:    # Read sides
    sides = float(input('Enter side:'))
    return sides


# Check if it is a square
def is_square(side_1, side_2, side_3, side_4) -> bool:
    if side_1 == side_2 == side_3 == side_4:
        return True
    return False


# Check if it is a rectangle
def is_rectangle(side_1, side_2, side_3, side_4) -> bool:
    if (side_1 ** 2) + (side_2 ** 2) == (side_3 ** 2) + (side_4 ** 2):
        return True
    return False


# Calculate rectangle area
def square_rectangle(side_1, side_2) -> float:
    return side_1 * side_2


# Asking the user to enter 4 sides
side_a = entered_sides()
side_b = entered_sides()
side_c = entered_sides()
side_d = entered_sides()


# Informing the user if it is a rectangle or square and their area
if is_rectangle(side_a, side_b, side_c, side_d):
    print(f'It\'s a rectangle. Area of rectangle is: {square_rectangle(side_a, side_b)}')
else:
    print('It\'s not a rectangle')


# Task 2
print('Task 2')


def generate_email(name, domain) -> str:
    random_number = randint(100, 999)
    random_string = ''.join(sample(ascii_lowercase, randint(5, 7)))
    domain = random.choice(domains)
    name = random.choice(names).lower()

    return f'{name}.{random_number}@{random_string}.{domain}'


names = ['Amazon', 'Google', 'Yahoo', 'Ebay', 'Aliexpress']
domains = ['com', 'ua', 'pro', 'com.ua', 'org']

print(generate_email(names, domains))

# Task 3
print('Task 3')
list_1 = [1, 5, 7, 9, 10, 11, 12, 19]
list_2 = [19, 7, 6, 2, 22, 18, 35, 9]

intersection = list(filter(lambda x: x in list_1, list_2))
print(intersection)

# Task 4
print('Task 4')
test_string = input('Enter any value:')

is_numeric = lambda x: x.isdigit()
print(is_numeric(test_string))

# Task 5
print('Task 5')
test_list = [[4, 6, '123', 11], [98], [], [54, 8, 'com'], [1, 4, 5, 6, 7, 8, 9, 10, 11]]

longest_list = list(reduce(lambda x, y: x if len(x) > len(y) else y, test_list))
shortest_list = list(reduce(lambda x, y: x if len(x) < len(y) else y, test_list))
print(f'Longest list is: {longest_list}')
print(f'Shortest list is: {shortest_list}')

# Task 6
print('Task 6')
list_of_numbers = [1, 3, 4, 5, 7, 11, 12, 5]

products_of_numbers = reduce(lambda x, y: x * y, list_of_numbers)
print(products_of_numbers)
