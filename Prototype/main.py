"""
Prototype Pattern
"""

from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Product(metaclass=ABCMeta):

    @abstractmethod
    def use(self):
        pass

    @abstractmethod
    def create_clone(self):
        pass

    def clone(self):
        obj = deepcopy(self)
        return obj

class Manager:
    def __init__(self):
        self.showcase = {}

    def register(self, name: str, proto: Product):
        self.showcase[name] = proto

    def create(self, proto_name: str):
        p = self.showcase[proto_name]
        return p.create_clone()


class MessageBox(Product):
    def __init__(self, decochar: str):
        self.decochar = decochar

    def use(self, s: str):
        length = len(s)
        for _ in range(length + 4):
            print(self.decochar, end="")
        print("")
        print(f"{self.decochar} {s} {self.decochar}")
        for _ in range(length + 4):
            print(self.decochar, end="")
        print("")

    def create_clone(self):
        p = None
        try:
            p = self.clone()
        except Exception as e:
            print(e)
        return p


class UnderlinePen(Product):
    def __init__(self, ulchar: str):
        self.ulchar = ulchar

    def use(self, s: str):
        length = len(s)
        print(f'"{s}"')
        print(" ", end="")
        for _ in range(length):
            print(self.ulchar, end="")
        print(" ")

    def create_clone(self):
        p = None
        try:
            p = self.clone()
        except Exception as e:
            print(e)
        return p


def main():
    manager = Manager()
    upen = UnderlinePen("~")
    mbox = MessageBox("*")
    sbox = MessageBox("/")
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)

    p1 = manager.create("strong message")
    p1.use("Hello, world.")
    p2 = manager.create("warning box")
    p2.use("Hello, world.")
    p3 = manager.create("slash box")
    p3.use("Hello, world.")


if __name__ == "__main__":
    main()
