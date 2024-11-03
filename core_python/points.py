class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{str(self.x)},{str(self.y)}"


from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    case _:
        print("Not a valid color")
var = 2
p1 = Point(1, var)
p3 = Point(3, y=var)
p2 = Point(y=var, x=1)

print(p1, p2, p3)
a = "x ".join("anc")
print("A:", a)


def concat(*args, sep="/"):
    return sep.join(args)


lst1 = [3, 15]
lst2 = [1, 5]

lst = [1, 2, 3]
print(concat("a", "b,", "c"))
print(" ".join(str(x) for x in lst))  # iterable not i
args = [3, 6]
print(list(range(*args)))
a = [(i - j) for i, j in zip(list(range(*lst1)), list(range(*lst2)))]
print(a)
