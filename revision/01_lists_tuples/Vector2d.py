import math
from array import array


class Vector2d:
    typecode = "d"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):

        return (i for i in (self.__x, self.__y))

    def __add__(self, other):
        return Vector2d(self.x + other.y, self.y + other.y)

    def __repr__(self):
        class_name = type(self).__name__
        return f"Vector({self.__x!r}, {self.__y!r})"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + (bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))


def main():
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3, 5)
    print(v1 + v2)
    print(v1)
    print(format(v1))
    print(repr(v1))
    print(bytes(v1))


if __name__ == "__main__":
    main()
