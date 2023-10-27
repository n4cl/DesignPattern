from abc import abstractmethod

class Aggregate:
    """
    Aggregate interface
    """
    @abstractmethod
    def iterator(self):
        pass

class Iterator:
    """
    Iterator interface
    """
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Book:
    """
    Book class
    """
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class BookShelf(Aggregate):
    """
    BookShelf class
    """

    def __init__(self, max_size):
        self.__books = [None] * max_size
        self.__last = 0

    def get_book_at(self, index):
        return self.__books[index]

    def append_book(self, book):
        self.__books[self.__last] = book
        self.__last += 1

    def get_length(self):
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)

class BookShelfIterator(Iterator):
    """
    BookShelfIterator class
    """
    def __init__(self, book_shelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def has_next(self):
        if self.__index < self.__book_shelf.get_length():
            return True
        else:
            return False

    def next(self):
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book


class Main:
    """
    Main class
    """
    def main(self):
        book_shelf = BookShelf(4)
        book_shelf.append_book(Book("Around the World in 80 Days"))
        book_shelf.append_book(Book("Bible"))
        book_shelf.append_book(Book("Cinderella"))
        book_shelf.append_book(Book("Daddy-Long-Legs"))
        it = book_shelf.iterator()
        while it.has_next():
            book = it.next()
            print(book.get_name())

        # 以下のような実装だと、BookShelf の実装に依存してしまう
        for i in range(book_shelf.get_length()):
            book = book_shelf.get_book_at(i)
            print(book.get_name())


if __name__ == '__main__':
    Main().main()
