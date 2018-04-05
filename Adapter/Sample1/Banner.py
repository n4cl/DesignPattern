# coding: utf-8


class Banner(object):
    """
    最初から提供されているとするクラス
    必要な機能を追加するのではなく、
    当クラスを継承して、必要な機能仕様を満たすようにする
    """

    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        print "(" + self.string + ")"

    def show_with_aster(self):
        print "*" + self.string + "*"
