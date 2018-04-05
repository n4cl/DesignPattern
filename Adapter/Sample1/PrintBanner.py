# coding: utf-8

from Banner import Banner
from Print import Print


class PrintBanner(Banner, Print):
    """
    Adapterとなるクラス
    Bannerクラスを継承し、Printクラスのinterfaceを実装する
    """

    def __init__(self, string):
        super(PrintBanner, self).__init__(string)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()
