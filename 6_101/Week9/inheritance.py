# x="xylophone"
class A:
    x = "ale"

    def __init__(self):
        self.x = self.x


class B(A):
    b = "bear"

    def __init__(self):
        super().__init__()
        self.x = "bat"


b = B()
print(b.x)


class C(A):
    u = "cat"

    def __init__(self):
        super().__init__()


c = C()
print(c.x)
print(C.x)


class D(A):
    e = "dog"

    def __init__(self):
        super().__init__()


d = D()
print(d.x)
print(c.b)
