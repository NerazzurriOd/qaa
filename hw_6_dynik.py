import re

# Task 1
print('Task 1')


def check_string(text):     # Create func to check string
    if re.match(r'^[\w]+$', text):
        print('This string contains only uppercase and lowercase letters, numbers, and underscores.')
    else:
        print('There are extra characters in this line')


check_string('Ab12_')
check_string('Ab12_.')
check_string('')


# Task 2
print('Task 2')


def delete_symbols(text):       # Create func to delete all data in brackets and delete brackets too
    print(re.sub(r'\([^)]*\)', '', text))


delete_symbols('example (.com)')
delete_symbols('github (.com)')
delete_symbols('stackoverflow (.com)')


# Task 3
print('Task 3')


def insert_space(text):     # Create func to insert space before capital letters
    print(re.sub(r'(?<=\w)([A-Z])', r" \1", text))


insert_space('lHelloHiWW WWW')
