# coding: utf-8

from PrintBanner import PrintBanner


def main():
    """
    Adapter: 委譲パターン
    """
    p = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == '__main__':
    main()
