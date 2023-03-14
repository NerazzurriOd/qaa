import random

# Task 1.
print('# Task 1')

random_list_1 = random.sample(range(1, 20), 10)
random_list_2 = random.sample(range(1, 20), 10)
print(f'First list: {random_list_1}, Second list: {random_list_2}')

same_numbers = list(set(random_list_1).intersection(set(random_list_2)))  # Create new list from intersection set
same_numbers.sort()  # Sort list of same numbers
print(same_numbers)

# Task 2.
print('# Task 2')
students = {
    'Ivan': 12,
    'Fedir': 7,
    'Olga': 9,
    'Marat': 4,
    'Petro': 6
}

average_mark = sum(students.values()) / len(students.items())

for student, score in students.items():
    if score > average_mark:
        print(f'Student {student} has mark {score} and it\'s greater than average {average_mark}!', end='\n')

# Task 3.
print('# Task 3')
random_list = random.choices(range(15), k=15)  # Create new list
print(random_list)  # Print list with random numbers

print(f'Number of different nums in list: {len(set(random_list))}')  # Print count of different nums in list

# Task 4.
print('# Task 4')
number_list_1 = random.sample(range(1, 20), 10)
number_list_2 = random.sample(range(1, 20), 10)

print(f'List 1: {number_list_1}\nList 2: {number_list_2}')  # Print both given lists

resulted_list = sorted(list(set(number_list_1).intersection(set(number_list_2))))
for number in resulted_list:
    print(number, end='\n')  # Numbers are printed in the new line

# Task 5.
print('# Task 5')
given_text = 'one two free one one free free two four'
dict_1 = {}  # Create new empty dictionary
for word in given_text.split():
    dict_1[word] = given_text.split().count(word)  # Fill the dictionary with words and their count

for item in dict_1.items():
    print(item, end=' ')  # Print results in the same line
