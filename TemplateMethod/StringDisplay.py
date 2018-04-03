# coding: utf-8

from AbstractDisplay import AbstractDisplay
from sys import stdout


class StringDisplay(AbstractDisplay):

    def __init__(self, _str):
        self.str = _str
        self.width = len(_str)

    def open(self):
        self.print_line()

    def output(self):
        print "|" + self.str + "|"

    def close(self):
        self.print_line()

    def print_line(self):
        stdout.write("+")

        for i in xrange(self.width):
            stdout.write("-")

        stdout.write("+\n")
