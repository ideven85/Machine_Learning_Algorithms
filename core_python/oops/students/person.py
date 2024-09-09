class Person:
    def __init__(self):
        self.name = "Charles"
        self.dob = self.Dob()

    def display(self):
        print("Name: ", self.name)

    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 1997

        def display(self):
            print("Dob: {}/{}/{}".format(self.dd, self.mm, self.yy))


p = Person()
p.display()
x = p.dob
x.display()
