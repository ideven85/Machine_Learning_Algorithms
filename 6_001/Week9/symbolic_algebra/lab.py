"""
6.101 Lab:
Symbolic Algebra
"""

import doctest


# NO ADDITIONAL IMPORTS ALLOWED!
# You are welcome to modify the classes below, as well as to implement new
# classes and helper functions as necessary.


# Remember At Least 10 hours per lab
class Symbol:
    # def __init__(self,n,left=None,right=None):
    #     self.n=n
    #     self.left=left
    #     self.right=right
    pass


class Var(Symbol):
    precedence = 2

    def __init__(self, n):
        """
        Initializer.  Store an instance variable called `name`, containing the
        value passed in to the initializer.
        """
        self.name = n

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Var('{self.name}')"


class Num(Symbol):
    precedence = 1

    def __init__(self, n):
        """
        Initializer.  Store an instance variable called `n`, containing the
        value passed in to the initializer.
        """
        self.n = n

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return f"Num({self.n})"


class BinOp(Symbol):
    wrap_right_at_same_precedence = False

    def __init__(self, left, right):
        temp = None

        # print(left, right)

        def match_symbol(temp):
            match1 = isinstance(temp, (float, int))
            match2 = isinstance(temp, str)

            match3 = isinstance(temp, BinOp)
            if match3:
                # precedence = temp.__class__.precedence
                # precedenceRight = temp.right.__class__.precedence
                # print(temp.left, temp.right)
                match_symbol(temp.left)
                match_symbol(temp.right)
            elif match1:
                temp = Num(temp)
            elif match2:
                temp = Var(temp)
            return temp

        self.left = match_symbol(left)
        self.right = match_symbol(right)

    def __repr__(self):
        return f"{str(self.__class__.__name__)}({repr(self.left)},{repr(self.right)})"

    # def __str__(self):
    #     return self.__class__.__str__
    #     #return f"{self.left} {self.__class__.operator} {self.right}"


class Div(BinOp):
    precedence = 2
    operator = "/"

    # def __repr__(self):
    #     return f"Div({repr(self.left)},{repr(self.right)})"

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"


class Mul(BinOp):
    precedence = 2
    operator = "*"

    # def __repr__(self):
    #     return f"Mul({repr(self.left)},{repr(self.right)})"

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"


class Add(BinOp):
    precedence = 1
    operator = "+"

    # def __init__(self, left, right):
    #     super().__init__(left, right)
    #
    # def __repr__(self):
    #     return f"Add({repr(self.left)},{repr(self.right)})"

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"


class Sub(BinOp):
    precedence = 1
    operator = "-"

    # def __repr__(self):
    #     return f"Sub({repr(self.left)},{repr(self.right)})"

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"


if __name__ == "__main__":
    """
    Add(Add(Var('x'), Num(3)), Num(2)) represents the symbolic expression x+3+2
    """
    doctest.testmod()
    # >> > z = Add(Var('x'), Sub(Var('y'), Num(2)))
    # >> > repr(z)  # notice that this result, if fed back into Python, produces an equivalent object.
    # "Add(Var('x'), Sub(Var('y'), Num(2)))"
    # >> > str(z)  # this result cannot necessarily be fed back into Python, but it looks nicer.
    "x + y - 2"
    x = Add(Mul(Var("x"), Sub(Var("y"), Num(2))), Var("z"))
    print(x)
    print(repr(x))

    y = Add(3, "x")
    # print(y)
    print(repr(y))
    print(y)
    print(y.__class__.__name__)
