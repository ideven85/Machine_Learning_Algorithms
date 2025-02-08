from dataclasses import dataclass
import random

@dataclass
class Demo:
    x=1
    y:int


    def __add__(self, other):
        return self.x + self.y + other.x + other.y

    def __hash__(self):
        random.seed(42)
        print(random.random())
        return self.x+self.y

    def __eq__(self, other):
        return type(other)==Demo and self.y == other.y and hash(self)==hash(other)


def main():
    d = Demo(2)
    y = Demo(3)
    e = Demo(2)
    print(d==e)
    print(d is e)
    print(d+y)
    print(hash(d))
    print(dir(d))
if __name__ == '__main__':
    main()