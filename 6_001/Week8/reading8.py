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


print(magnitude(v))


print(v.__class__.__base__)
