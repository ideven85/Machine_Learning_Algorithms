from revision.oops.StudentSubjects import StudentSubjects

#todo Doubt Regarding super constructor,when passing self..Means Instance of itself..
class Student:
    # this is a class variable
    n = 0
    def __init__(self,name='.',marks=0,subjects='Maths'):
        self.name = name
        self.marks =marks
        self.subjects =subjects
        self.display=StudentSubjects(self).display()
        Student.n +=1
    @staticmethod
    def numberOfStudents():
        print('Number of Students:',Student.n)








class Sample:
    x=10

    @classmethod # Same as static method in Java.. Property belongs to class variable not
    # instance variable
    def modify(cls):
        cls.x+=1

    @staticmethod
    def display(e):
        e.marks+=100
        e.display()

class TestStudent(Student):
    def __init__(self,name='.',marks=0,subjects='Maths'):
        super().__init__(name,marks,subjects)




s1 = Sample(); s2 = Sample()
print('x in s1=',s1.x)
print('x in s2=',s2.x)
s1.modify()
print('x in s1=',s1.x)
print('x in s2=',s2.x)

Deven = Student('Deven',80,'Computer Science')

Dave = Student('Dave',70)
Student.numberOfStudents()

#Deven.display
