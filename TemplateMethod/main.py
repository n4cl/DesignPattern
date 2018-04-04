# coding: utf-8

from CharDisplay import CharDisplay
from StringDisplay import StringDisplay


def main():
    """
    各クラスのスーパークラスで一連の処理を共通化している
    """
    d1 = CharDisplay("H")
    d2 = StringDisplay("Hello World")
    d3 = StringDisplay(u"こんにちわ")

    d1.display()
    d2.display()
    d3.display()


if __name__ == '__main__':
    main()
