from abc import ABCMeta, abstractmethod
from unicodedata import east_asian_width

class AbstractDisplay(metaclass=ABCMeta):
    """
    AbstractClass
    """

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()

        for _ in range(5):
            self.print()

        self.close()


class CharDisplay(AbstractDisplay):

    def __init__(self, ch: str):
        if len(ch) != 1:
            raise ValueError("ch must be 1 character")
        self.ch = ch

    def open(self):
        print("<<", end="")

    def print(self):
        print(self.ch, end="")

    def close(self):
        print(">>")


class StringDisplay(AbstractDisplay):

    def __init__(self, _str):
        self.str = _str
        self.width = 0
        for s in _str:
            t = east_asian_width(s)
            if t ==  "W" or t == "F" or t == "A":
                self.width += 2
            else:
                self.width += 1

    def open(self):
        self.print_line()

    def print(self):
        print(f"|{self.str}|")

    def close(self):
        self.print_line()

    def print_line(self):
        print("+", end="")

        for _ in range(self.width):
            print("-", end="")

        print("+")

def main():
    """
    各クラスのスーパークラスで一連の処理を共通化している
    """
    d1 = CharDisplay("H")
    d2 = StringDisplay("Hello World")
    d3 = StringDisplay("こんにちは。")

    d1.display()
    d2.display()
    d3.display()


if __name__ == '__main__':
    main()
