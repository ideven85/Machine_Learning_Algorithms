class Student:
    x = 10

    def __init__(self, id_=None):
        self.id_ = id_

    """
    Student object will have these attributes by default
'__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 ]
    """


obj = Student(100)
obj.__dict__["name"] = "John"
print(type(obj), len(obj.__dict__))
s1 = Student()
print(dir(s1))


class S2:
    x = 1


s2 = S2()
print(dir(s2))
