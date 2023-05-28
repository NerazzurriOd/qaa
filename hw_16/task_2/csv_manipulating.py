import csv


def add_str(file, data):
    with open(file, 'a', newline='') as csv_file:
        csv.writer(csv_file).writerow(data)


def del_str(file):
    with open(file, 'r') as csv_file:
        lines = csv_file.readlines()
        if not lines:
            print('File is empty')

    with open(file, 'w', newline='') as csv_file:
        csv_file.writelines(lines[:-1])
