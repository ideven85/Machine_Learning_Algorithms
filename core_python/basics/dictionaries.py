import random

table = dict()


class A:
    def __init__(self):
        self.items = [32, 33]


a = A()
vals = ({"A": 1}, {"B": 2}, {"A": 3})
i = 0
for val in vals:
    for key, value in val.items():
        table.setdefault(key, []).append(value)
    i += 1


print(table)
print(list(table.keys())[0])
random.seed(42)
