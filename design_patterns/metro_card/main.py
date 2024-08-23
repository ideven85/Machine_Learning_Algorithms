# Design Pattern, just a mockup
from dataclasses import dataclass


@dataclass
class MetroCard:
    money: float
    number: int


def load_data():
    lst = []
    with open("inputs/input1.txt", "r") as f:
        data = f.read()
    for line in data.split("\n"):
        lst.append(line)
    print(lst)


def main():
    load_data()


main()
