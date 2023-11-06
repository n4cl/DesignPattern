class Singleton:
    __singleton = None

    def __init__(self) -> None:
        print("インスタンスを生成しました。")

    @classmethod
    def initialize(cls):
        cls.__singleton = Singleton()

    @classmethod
    def getInstance(cls):
        return cls.__singleton


def main():
    print("Start.")
    Singleton.initialize()
    obj1 = Singleton.getInstance()
    obj2 = Singleton.getInstance()
    if obj1 == obj2:
        print("obj1とobj2は同じインスタンスです。")
    else:
        print("obj1とobj2は同じインスタンスではありません。")
    print("End.")


if __name__ == "__main__":
    main()

