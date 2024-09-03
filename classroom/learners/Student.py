from classroom.general.Person import Person


class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        # self._name=self._name
        # self._age=self._age

        self._grade = grade

    # @property
    # def grade(self,grade):
    #     self._grade = grade

    def __str__(self):
        return f"{self._name} aged {self._age} is in class {self._grade}"
    
    
        