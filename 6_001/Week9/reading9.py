x = "Global Object"


class A:
    x = "A Instance Variable"


class B(A):
    x = "B instance variable"

    def __init__(self):
        self.x = x


class C(B):
    x = "C instance variable"

    def __init__(self):
        super().__init__()
        self.x=self.x




a = A()
print(a.x)
print(A.x)
b = B()
print("B Object:", b.x)
print("B Class:", B.x)
c = C()
print("C Object:", c.x)
print("C class", C.x)
