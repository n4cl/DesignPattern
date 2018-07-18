# coding: utf-8

from abc import ABCMeta, abstractmethod


class Factory(object):

    __metaclass__ = ABCMeta

    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass
