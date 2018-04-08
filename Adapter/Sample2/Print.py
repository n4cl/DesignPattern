# coding: utf-8

from abc import ABCMeta, abstractmethod


class Print(object):
    """
    必要とされる仕様
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass
