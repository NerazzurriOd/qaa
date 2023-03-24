import re

# Task 1
print('Task 1')


def get_domains(file_name):     # Create func to get domains
    with open(file_name) as file:
        # Loop through the lines of the file with space removal and deletion of dots in the lines
        domain = [line.strip().replace('.', '') for line in file]
    return domain


domains = get_domains('domains.txt')
print(domains)

# Task 2
print('Task 2')


def get_surnames_from_file(file_name):      # Create func to receive surnames from file
    surnames = []       # Create empty list
    with open(file_name, 'r') as file:
        for line in file:
            fields = re.split(r'[,._-]\s*', line)       # Split strings in list
            surnames.append(fields[1])      # Add surnames to final list
    return surnames


surnames = get_surnames_from_file('names.txt')
print(surnames)


# Task 3
print('Task 3')


def get_dates(filename):        # Create func to find date in file
    result = []     # Create empty list for future result
    with open(filename) as file:
        for line in file:
            # Find date with format ex: '1st march 1987'
            resulted_date = re.search(r'\d{1,2}\w{2}\s\w+\s\d{4}', line)
            if resulted_date:       # If date present
                date = resulted_date.group()    # create a readable string
                result.append({'date': date})   # Add string to final list
    return result


dates = get_dates('authors.txt')
print(dates)
