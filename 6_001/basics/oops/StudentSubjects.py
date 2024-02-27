class StudentSubjects:
    def __init__(self,student):
        self.marks = student.marks
        self.name = student.name
        self.subjects = student.subjects

    def display(self):
        print('Name:',self.name)
        print('Marks:',self.marks)
        print('Subjects:',self.subjects)
