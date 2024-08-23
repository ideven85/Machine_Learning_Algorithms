# x="xylophone"
class A:
    x = "ale"

    def __init__(self):
        self.x = self.x


class B(A):
    x = "bear"

    def __init__(self):
        super().__init__()
        self.x = "bat"


b = B()
print(b.x)


class C(B):
    x = "cat"

    def __init__(self):
        pass


c = C()
print(c.x)
print(C.x)


class D(C):
    x = "dog"

    def __init__(self):
        super().__init__()


d = D()
print(d.x)
