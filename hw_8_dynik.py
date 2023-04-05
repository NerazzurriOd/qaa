from modules.math_operations.operations_with_two_digits import add_two_numbers
from modules.math_operations.operations_with_two_digits import multiply_two_numbers
from modules.math_operations.operations_with_two_digits import subtraction_two_numbers
from modules.math_operations.operations_with_two_digits import division_two_numbers
from modules.string_operations.string_lower_upper_case import string_to_lower_case
from modules.string_operations.string_lower_upper_case import string_to_upper_case


# Task 1
print(add_two_numbers(4, 5))
print(multiply_two_numbers(17, 22))
print(subtraction_two_numbers(16, 4))
print(division_two_numbers(20, 5))
print(string_to_lower_case('ABCDEFG'))
print(string_to_upper_case('main person'))


# Task 2
list_1 = [6, 'a', {'a'}, [1, 2, 3], 0]
num_1 = 4
dict_1 = {'1': "aa", '2': "bb", '3': "cc"}


def check_errors1(list1, num):
    for i in range(10):
        try:
            print(num / list1[i])
        except TypeError:
            print('Type error')
            continue
        except ZeroDivisionError:
            print('Zero Division Error')
            continue
        except IndexError:
            print('Index Error')


def check_errors2(dict1, num):
    try:
        print(dict1[4] / num)
    except KeyError:
        print('Key Error')


check_errors1(list_1, num_1)
check_errors2(dict_1, num_1)


# Task 3
from datetime import datetime, timedelta


def add_or_subtract(date, days, sign=True):
    if sign:
        print(date + timedelta(days=days))
    else:
        print(date - timedelta(days=days))


add_or_subtract(datetime(2020, 2, 15), 15, True)
add_or_subtract(datetime(2020, 2, 15), 15, False)


# Task 4
def calculate_age(birthdate):
    now = datetime.now()
    age_timedelta = now - birthdate
    print(age_timedelta)
    return now, now.timestamp()


birthdate = datetime(1995, 6, 15, 12, 0, 0)
now, timestamp = calculate_age(birthdate)
print(timestamp)
print('Ваш возраст', timestamp // (60 * 60 * 24 * 365.25), 'лет')
