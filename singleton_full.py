# -*- coding: utf-8 -*-


class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances


if __name__ == "__main__":
    class Logger(Singleton):
        pass

    a = Logger()
    b = Logger()
    print(a)
    print(b)
