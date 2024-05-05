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
    def __init__(self, n):
        """
        Initializer.  Store an instance variable called `name`, containing the
        value passed in to the initializer.
        """
        self.name = n

    def __str__(self):
        return str(self.name)


class Var(Symbol):

    def __repr__(self):
        return f"Var('{self.name}')"


class Num(Symbol):

    def __repr__(self):
        return f"Num({self.name})"


def match_num(var):
    # print(var)
    return True if isinstance(var, (float, int, Num)) else False


def match_str(var):
    return True if isinstance(var, (str, Var)) else False


class BinOp:

    def temp(self, expr, values=None):
        pass

    def __init__(self, left, right):
        if isinstance(left, BinOp):

            print(left.left, left.right)
            input("left")
        if isinstance(right, BinOp):
            print(right.left, right.right)
            # left=right.left
            # right=right.right
            input("Right")

        if match_num(left):
            self.left = Num(left)
        if match_str(left):
            self.left = Var(left)
        if match_num(right):
            self.right = Num(right)
        if match_str(right):
            self.right = Var(right)
        # else:
        #     if left:
        #         if match_num(left):
        #             self.left=Num(left)
        #         if match_str(left):
        #             self.left=Var(left)
        #         else:
        #             self.__init__(left, right)
        #     if right:
        #         if match_num(right):
        #             self.right=Num(right)
        #         if match_str(right):
        #             self.right=Var(right)
        #         else:
        #             self.__init__(left, right)
        else:
            self.left = left
            self.right = right


class Div(BinOp):

    precedence = 2

    def __repr__(self):
        return f"Div({repr(self.left)},{repr(self.right)})"

    def __str__(self):
        return f"{self.left}/{self.right}"


class Mul(BinOp):
    precedence = 1

    def __repr__(self):
        return f"Mul({repr(self.left)},{repr(self.right)})"

    def __str__(self):
        return f"{self.left}*{self.right}"


"""
These constructors should also accept integers, floats, or strings as their arguments. Add(2, 'x'),
 for example, should create an instance Add(Num(2), Var('x')).
  It is okay to use isinstance or type in this context, to check if the arguments passed to the constructor
   are strings or numbers.
"""


class Add(BinOp):

    precedence = 0

    def __init__(self, left, right):

        super().__init__(left, right)

    # def __repr__(self):
    #     return f"Add({repr(self.left)},{repr(self.right)})"

    # def __str__(self):
    #     if isinstance(self.left,BinOp) and isinstance(self.right,BinOp):
    #         return f"{self.left}+{self.right}"
    #     elif isinstance(self.right,BinOp):
    #         return f"Right{self.left}+({self.right})"
    #     elif isinstance(self.left, BinOp):
    #         return f"Left({self.left})+{self.right}"
    #     else:
    #         return f"Plain{self.left}+{self.right}"

    # def __str__(self):
    #     return f"{self.left}+{self.right}"


class Sub(BinOp):

    precedence = 0

    def __repr__(self):
        return f"Sub({repr(self.left)},{repr(self.right)})"

    def __str__(self):
        return f"{self.left}-{self.right}"


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
    x = Add(Add(Var("x"), Add(Num("y"), Num(2))), Var("z"))
    # print(x)
    print(x.right)
    # z = Add(Var('x'), Sub(Var('y'), Num(2)))
    # print(repr(z))
    # print(z)
    # precedence Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
    """
    If B.left and/or B.right themselves represent expressions with lower precedence than B, wrap their string representations in parentheses (here, precedence is defined using the standard "PEMDAS" ordering).
As a special case, if B represents a subtraction or a division and B.right represents an expression with the same precedence as B, wrap B.right's string representation in parentheses.
Individual numbers or variables should never be wrapped in parentheses.

Check Yourself:
Think about the rules for parenthesization described above in terms of algebraic expressions and work through parenthesizing some example expressions by hand to get a feel for how these rules work. Do these rules seem to work in a general sense -- will they always work across different operations and across different levels of expression complexity? Why do they work? Why are subtraction and division treated differently from addition and multiplication?

Check Yourself:
Importantly, you should implement the behavior for str and repr without explicitly checking the type of self, self.left, or self.right.

In order to pass the test cases, your code will need to do this by storing a couple of additional class attributes:

All symbols should have a class attribute called precedence, which should be a number representing precedence. Greater numbers should represent greater precedence. What classes should have the highest precedence? What classes should have the same precedence?
All binary operations should have a class attribute called wrap_right_at_same_precedence, which should be a Boolean that indicates whether to add parentheses around the right side of the expression in the special case described above.
    """
    # y=Add(3,Add(4,'x'))
    # # print(y)
    # print(repr(y))
    # print(y)
    # a=Add(2,'x')
    # print(a)
    # print(repr(a))
    # a1=Mul(Var('x'), Add(Var('y'), Var('z')))
    # print(a1)
    # print(repr(a1))
    # print(a1.left)
    # print(y.left)
    # print(y.right)
