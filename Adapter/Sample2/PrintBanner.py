# coding: utf-8

from Banner import Banner
from Print import Print


class PrintBanner(Print):
    """
    Adapterとなるクラス
    Bannerクラスに委譲する
    """

    def __init__(self, string):
        self.banner = Banner(string)

    def print_weak(self):
        self.banner.show_with_aster()

    def print_strong(self):
        self.banner.show_with_aster()
