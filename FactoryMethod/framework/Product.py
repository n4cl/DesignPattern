# coding: utf-8

from abc import ABCMeta, abstractmethod


class Product(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def use(self):
        pass
