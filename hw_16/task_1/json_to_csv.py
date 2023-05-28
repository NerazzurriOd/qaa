import csv
import json


class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r', newline='') as json_file:
            self.__lines = json.load(json_file)
            print(self.__lines)

    def write_file(self, filename: str):
        with open(filename, 'w', newline='') as csv_file:
            headers = self.__lines[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.__lines)


converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('file.csv')





