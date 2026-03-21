from abc import ABC, abstractmethod
from traceback import print_tb


#abstrakt klass

class Printable(ABC):
    #abstrakt method
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f"Book : {self.title}, by:{self.author}")

book = Book("Bageti e Bujqesi", "Naim Frasheri")
book.print_info()