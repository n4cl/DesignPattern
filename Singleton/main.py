import threading

class Singleton:
    __singleton = None
    __lock = threading.Lock()

    def __init__(self) -> None:
        print("インスタンスを生成しました。")

    @classmethod
    def __initialize(cls):
        cls.__singleton = Singleton()

    @classmethod
    def get_instance(cls):
        """
        マルチスレッド下での動作を考慮していない
        """
        if cls.__singleton is None:
            cls.__initialize()
        return cls.__singleton

    @classmethod
    def get_instance_thread_safe(cls):
        """
        マルチスレッド下での動作を考慮した場合
        """
        # ロックを取得するオーバーヘッドを避けるため
        if cls.__singleton is None:
            with cls.__lock:
                # ロック解放後にすでにインスタンスが生成されている可能性があるため
                if cls.__singleton is None:
                    cls.__initialize()
        return cls.__singleton


def main():
    print("Start.")
    obj1 = Singleton.get_instance()
    obj2 = Singleton.get_instance()
    obj3 = Singleton.get_instance_thread_safe()
    if obj1 == obj2 == obj3:
        print("obj1とobj2とobj3は同じインスタンスです。")
    else:
        print("obj1とobj2とobj3は同じインスタンスではありません。")
    print("End.")


if __name__ == "__main__":
    main()

