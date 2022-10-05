# -*- coding: utf-8 -*-


from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


if __name__ == '__main__':
    alex = User('Alex', 39)

    print(alex == alex)
    print(alex.name)
    print(alex)
