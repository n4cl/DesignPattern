# coding: utf-8

from AbstractDisplay import AbstractDisplay
from sys import stdout


class CharDisplay(AbstractDisplay):

    def __init__(self, ch):
        self.ch = ch

    def open(self):
        stdout.write("<<")

    def output(self):
        stdout.write(self.ch)

    def close(self):
        stdout.write(">>\n")
