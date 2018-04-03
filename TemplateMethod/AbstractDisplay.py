# coding: utf-8

from abc import ABCMeta, abstractmethod


class AbstractDisplay(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def open(self):
        pass

    # print を利用できないため名前を変更
    @abstractmethod
    def output(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        """
        Template Method
            displayメソッドでサブクラスの処理を共通化する
        """

        self.open()

        for i in xrange(5):
            self.output()

        self.close()
