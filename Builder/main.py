"""
Builder Pattern
"""
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def make_title(self, title: str):
        pass

    @abstractmethod
    def make_string(self, string: str):
        pass

    @abstractmethod
    def make_items(self, items: list):
        pass

    @abstractmethod
    def close(self):
        pass


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct(self):
        self.builder.make_title("Greeting")
        self.builder.make_string("朝から昼にかけて")
        self.builder.make_items(["おはようございます。", "こんにちは。"])
        self.builder.make_string("夜に")
        self.builder.make_items(["こんばんは。", "おやすみなさい。", "さようなら。"])
        self.builder.close()


class TextBuilder(Builder):
    def __init__(self):
        self.buffer = []

    def make_title(self, title: str):
        self.buffer.append("==============================\n")
        self.buffer.append(f"『{title}』\n")
        self.buffer.append("\n")

    def make_string(self, string: str):
        self.buffer.append(f"■{string}\n")
        self.buffer.append("\n")

    def make_items(self, items: list):
        for item in items:
            self.buffer.append(f"　・{item}\n")
        self.buffer.append("\n")

    def close(self):
        self.buffer.append("==============================\n")

    def get_result(self):
        return "".join(self.buffer)


class HTMLBuilder(Builder):
    def __init__(self):
        self.filename = None
        self.writer = None

    def make_title(self, title: str):
        self.filename = f"{title}.html"
        try:
            self.writer = open(self.filename, "w")
        except Exception as e:
            print(e)
        self.writer.write(f"<html><head><title>{title}</title></head><body>")
        self.writer.write(f"<h1>{title}</h1>")

    def make_string(self, string: str):
        self.writer.write(f"<p>{string}</p>")

    def make_items(self, items: list):
        self.writer.write("<ul>")
        for item in items:
            self.writer.write(f"<li>{item}</li>")
        self.writer.write("</ul>")

    def close(self):
        self.writer.write("</body></html>")
        self.writer.close()

    def get_result(self):
        return self.filename


def main():
    text_builder = TextBuilder()
    director = Director(text_builder)
    director.construct()
    result = text_builder.get_result()
    print(result)

    html_builder = HTMLBuilder()
    director = Director(html_builder)
    director.construct()
    filename = html_builder.get_result()
    print(f"{filename}が作成されました。")

if __name__ == "__main__":
    main()
