# coding: utf-8


class Banner(object):
    """
    最初から提供されているとするクラス
    """

    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        print "(" + self.string + ")"

    def show_with_aster(self):
        print "*" + self.string + "*"
