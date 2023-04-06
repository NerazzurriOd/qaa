import csv
import time


# Task 1
def read_csv_file(filename):    # Create function for reading file
    rows = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)
    return rows


def write_csv_file(filename, data):     # Create function for write data to file
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i in data:
            csv_writer.writerow(i)


# Create file
data = [
    ['Manufacturer', 'Brand', 'Year', 'Engine'],
    ['BMW', 'M5', '2020', 'Gas'],
    ['Opel', 'Astra', '1990', 'Diesel'],
    ['Kia', 'Optima', '2018', 'Hybrid']
]

write_csv_file('data.csv', data)


# Read file
read_data = read_csv_file('data.csv')


# Add data
new_data = [
    ['Hyundai', 'Sonata', '2017', 'Gas'],
    ['Tesla', 'Model S', '2019', 'Electric']
]

updated_data = read_data + new_data     # Update file


write_csv_file('data_new.csv', updated_data)    # Write data to the new file


# Task 2
def number_squares():
    for i in range(0, 100001):
        print(i**2)
        time.sleep(0.2)


number_squares()
