# 練習問題

from main import Aggregate, BookShelfIterator

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

        if self.__last < self.get_length():
            self.__books[self.__last] = book
        else:
            self.__books.append(book)
        self.__last += 1

    def get_length(self):
        return len(self.__books)

    def iterator(self):
        return BookShelfIterator(self)


def main():
    book_shelf = BookShelf(4)
    book_shelf.append_book("Around the World in 80 Days")
    book_shelf.append_book("Bible")
    book_shelf.append_book("Cinderella")
    book_shelf.append_book("Daddy-Long-Legs")
    book_shelf.append_book("Test1")
    book_shelf.append_book("Test2")
    it = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(book)


if __name__ == '__main__':
    main()
