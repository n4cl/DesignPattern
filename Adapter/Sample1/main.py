# coding: utf-8

from PrintBanner import PrintBanner


def main():
    """
    Bannerがどのような実装になっているか隠蔽されている
    """
    p = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == '__main__':
    main()
