from abc import ABC, abstractmethod


class Painting(ABC):
    def __init__(self):
        self._author = None
        self._title = None
        self._year = None
        self._price = None
        self.copies_number = None

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = new_year

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    def display_info(self):
        print(f'Title: {self._title}')
        print(f'Artist: {self._author}')
        print(f'Year: {self._year}')
        print(f'Price: {self.price}')
        print(f'Number of copies: {self.copies_number}')

    def sell_painting(self, count):
        if count > self.copies_number:
            print(f'You can\'t buy so many copies. We have only {self.copies_number} copies in stock')
        else:
            self.copies_number -= count
            print(f'Recently we\'ve sold {count} copies. Now we have {self.copies_number} copies in stock')

    def add_painting(self, count):
        self.copies_number += count
        print(f'Author has painted {count} copies. Now we have {self.copies_number} copies in stock')

    @abstractmethod
    def delivery(self):
        """Should implement delivery type"""

    def history(self):
        print('Short story')


class Picture(Painting):
    def __init__(self, author, title, price, year, copies_number):
        super().__init__()
        self.author = author
        self.title = title
        self.year = year
        self.price = price
        self.copies_number = copies_number

    def delivery(self):
        print('We deliver pictures every Monday')

    def history(self):
        print('Place for history about picture')


class Sculpture(Painting):
    def __init__(self, author, title, price, year, copies_number):
        super().__init__()
        self.author = author
        self.title = title
        self.year = year
        self.price = price
        self.copies_number = copies_number

    def delivery(self):
        print('We deliver sculptures every Friday')

    def history(self):
        print('Place for history about sculpture')


black_square = Picture('Malevich', 'Black Square', 20000000, 1915, 1)
black_square.display_info()
black_square.add_painting(3)
black_square.sell_painting(1)

david = Sculpture('Michelangelo Buonarroti', 'David', 'Not for sale', 1504, 1)
black_square.display_info()
