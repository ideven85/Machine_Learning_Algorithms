class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise TypeError("name must be a string")
        else:
            self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be less than zero")
        else:
            self._age = age

    def __repr__(self):
        raise TypeError("Must be implemented by base class")

    def __str__(self):
        raise TypeError("Must be implemented by base class")

