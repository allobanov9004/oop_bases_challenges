"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as jsonfile:
            return json.load(jsonfile)


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=',')
            return [row for row in csv_reader]


if __name__ == '__main__':
    file_reader = FileHandler('data\text.txt')
    print(file_reader.read())
    json_reader = JSONHandler('data\recipes.json')
    print(json_reader.read())
    csv_reader = CSVHandler('data\user_info.csv')
    print(csv_reader.read())
