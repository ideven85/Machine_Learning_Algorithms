import functools
from operator import itemgetter
from typing import List
from functools import cmp_to_key
from attr import dataclass


class Task:
    id: int
    name: str

    def __str__(self):
        return self.name + " " + str(self.id)

    def __repr__(self):
        return str(self)

    def __init__(self, id=None, name=None):
        self.id, self.name = id, name

    def comparator(a, b):

        return 1 if a.name > b.name or a.id > b.id else -1


def largest_number_can_be_formed(l: str) -> str:
    def value_comparator(x1, x2):
        if len(x1) == 0 or len(x2) == 0:
            return
        if len(x1) == 0:
            return x2
        if len(x2) == 0:
            return x1
        order1 = x1 + x2
        print(order1)
        order2 = x2 + x1
        return order1 if int(order1[0]) > int(order2[0]) else order2

    if not l or len(l) <= 2:
        return l
    mapping = dict()
    numbers = list(l)
    numbers = sorted(numbers, key=cmp_to_key(value_comparator))
    return "".join(numbers)


def largest_task(task1, task2):
    # id1,name1 = task1
    # id2,name2 = task2
    data = list()
    data.append(task1)
    data.append(task2)
    # task1 = sorted(task1,key=functools.cmp_to_key(Task.comparator))
    # task2 = sorted(task2,key=functools.cmp_to_key(Task.comparator))
    data = sorted(data, key=functools.cmp_to_key(Task.comparator))
    return data


def main():
    task1 = Task(1, "Deven")
    task2 = Task(1, "Dev")
    print(largest_task(task1, task2))
    # largest_number = "696171"
    # print(largest_number_can_be_formed(largest_number))


if __name__ == "__main__":
    main()
