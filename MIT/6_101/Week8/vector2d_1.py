class Vector2D:
    ndims = 2

    def magnitude(vec):
        return (vec.x**2 + vec.y**2) ** 0.5


v = Vector2D()
v.x = 3
v.y = 4

print(Vector2D.magnitude(v))

# How?
"""
It turns out that Python is doing some magic to make things work out this way.
 The actual details are somewhat complicated, but one way that we can think about what Python is doing is: 
 when we look up a method by way of an instance,
  Python figures out what class that's an instance of, 
  finds the given method within that class, and then implicitly passes in that instance as the first argument.
   So we can think of this as a transformation where the call v.magnitude() is turned into Vector2D.magnitude(v):


"""
print(v.magnitude())

# print(v.magnitude(v)) # This clears a lot of doubts I had experienced in the past
"""



he error message we see here is:
TypeError: Vector2D.magnitude() takes 1 positional argument but 2 were given
Until you get used to it (and even for a while afterwards...), this can be extremely confusing (What do you mean, Python? I only gave it one argument!!).

What's going on here, though, is that Python is implicitly providing v (the instance we used to look up the method) as the first argument; 
and then whatever arguments we provide are passed in afterwards. So even though what we wrote is v.magnitude(v), thinking about the transformation we mentioned above,
 that's equivalent to writing Vector2D.magnitude(v, v), where the second v is the one we provided explicitly, and the first was provided implicitly by Python.
"""


class Vector2D2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __bool__(self):
        return self.x or self.y
