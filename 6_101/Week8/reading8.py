# class Vector2D:
#     pass
#
#
# v = Vector2D()
# v.x = 3
# v.y = 4
#
#
# def magnitude(vec):
#     return (vec.x ** 2 + vec.y ** 2) ** 0.5
#
# print(v.magnitude(v))


class Vector2D:
    pass


v = Vector2D()
v.x = 3
v.y = 4


def magnitude(vec):
    return (vec.x**2 + vec.y**2) ** 0.5


# print(magnitude(v))
#
#
# print(v.__class__.__base__)

x = 20
"""
To look up an attribute inside of an object:

look in the object itself
if not found, look in that object's class
if not found, look in that class's superclass
if not found, look in that class's superclass
 (keep following that process, looking in superclasses)
if not found and no more superclasses, raise an AttributeError
"""


class A:
    x = "cat"


a = A()
print(a.x)
