from abc import ABCMeta, abstractmethod


class Banner:
    """
    最初から提供されているとするクラス
    """

    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        print(f"({self.string})")

    def show_with_aster(self):
        print(f"*{self.string}*")


class Print(metaclass=ABCMeta):
    """
    必要とされる仕様
    """

    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass


class PrintBanner(Print):
    """
    Adapterとなるクラス
    Bannerクラスに委譲する
    """

    def __init__(self, string):
        self.banner = Banner(string)

    def print_weak(self):
        self.banner.show_with_paren()

    def print_strong(self):
        self.banner.show_with_aster()

def main():
    """
    Adapter: 委譲パターン
    """
    p = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == '__main__':
    main()
