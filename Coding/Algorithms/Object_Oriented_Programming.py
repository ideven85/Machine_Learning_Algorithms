import abc
from abc import ABCMeta


class Employee(abc.ABC):
    def __init__(self):
        self.name = None
        self.age = None
        self.salary = None
        self.department = None
        self.rank = None

    @abc.abstractmethod
    def getSalary(self):
        pass


class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.rank = "Manager"
        self.salary = 100000

    def getSalary(self):
        return self.salary
