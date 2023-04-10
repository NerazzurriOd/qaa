from random import randint


# Task 1
def simple_function(func):
    def inner(*args, **kwargs):
        print(f'We are calling function {func.__name__}')
        return func(*args, **kwargs)
    return inner


@simple_function
def add_function(num1, num2):
    print(f'Sum of digits {num1} and {num2} is equal to: {num1 + num2}')


@simple_function
def multiply_function(num1, num2):
    print(f'Multiplication of the numbers {num1} and {num2} is equal to {num1 * num2}')


add_function(5, 10)
multiply_function(2, 5)


# Task 2
list_of_numbers = [randint(1, 10) for item in range(1, 101)]
print(list_of_numbers)
dict_count_numbers = {num: list_of_numbers.count(num) for num in set(list_of_numbers)}
for num, count in dict_count_numbers.items():
    print(f'{num}: {count}')
