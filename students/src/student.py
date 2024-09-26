from students.src.person import Person


class Student(Person):
    def __init__(self, grade):
        # self.name=super(self.name)
        # self.age=super(self.age)
        self._grade = grade

    def __repr__(self):
        return "Student is in grade " + str(self._grade)

    def __str__(self):
        return f"{self.name} of {self.age} is in {self._grade} class"
