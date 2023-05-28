import csv


def count_lines(file):
    total_lines = 0
    with open(file, 'r', newline='') as file:
        file_reader = csv.reader(file)
        for line in file_reader:
            total_lines += 1
    return total_lines
