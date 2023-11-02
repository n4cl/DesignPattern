from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):

    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):
    def create(self, owner):
        """
        抽象クラスでインスタンス生成を行うメソッドを定義する。
        """
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractmethod
    def create_product(self, owner):
        pass

    @abstractmethod
    def register_product(self, product):
        pass


class IDCard(Product):
    def __init__(self, owner):
        print(f"{owner}のカードを作ります。")
        self.owner = owner

    def use(self):
        print(f"{self.owner}のカードを使います。")

    def get_owner(self):
        return self.owner


class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.owners.append(product.get_owner())

    def get_owners(self):
        return self.owners


if __name__ == "__main__":
    factory = IDCardFactory()
    card1 = factory.create("結城浩")
    card2 = factory.create("とむら")
    card3 = factory.create("佐藤花子")
    card1.use()
    card2.use()
    card3.use()
