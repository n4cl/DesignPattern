# coding: utf-8

from framework.Product import Product


class IDCard(Product):
    def __init__(self, owner):
        print owner + u"のカードを作ります。"
        self.owner = owner

    def use(self):
        print self.owner + u"のカードを使います。"

    def get_owner(self):
        return self.owner
