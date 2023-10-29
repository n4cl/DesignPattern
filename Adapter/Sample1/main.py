from abc import abstractmethod, ABCMeta

class Banner:
    """
    最初から提供されているとするクラス
    必要な機能を追加するのではなく、
    当クラスを継承して、必要な機能仕様を満たすようにする
    """

    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        print(f"({self.string})")

    def show_with_aster(self):
        print(f"*{self.string}*")

class Print(metaclass=ABCMeta):
    """
    interface の役割
    必要とされる仕様
    """

    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass

class PrintBanner(Banner, Print):
    """
    Adapterとなるクラス
    Bannerクラスを継承し、Printクラスのinterfaceを実装する
    """

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()


def main():
    """
    Adapter: 継承パターン
    Bannerがどのような実装になっているか隠蔽されている
    """
    p = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == '__main__':
    main()
