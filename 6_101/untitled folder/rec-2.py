# 6.101 recitation: lab 10 wrapup

############################################ Expression classes


class Expr:
    pass


class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Var({repr(self.name)})"


class Num(Expr):
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return f"Num({repr(self.n)})"


class BinOp(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.left)},{repr(self.right)})"


class Add(BinOp):
    pass


class Sub(BinOp):
    pass


class Mul(BinOp):
    pass


class Div(BinOp):
    pass


############################################ Tokenizing


def tokenize(string):
    """
    If string is a symbolic algebra expression,
    returns list of tokens in the expression.

    >>> tokenize('(23* ( y + z ))')
    ['(', '23', '*' '(', 'y', '+', 'z', ')', ')']
    """
    pass


# Assume that tokenize() is already implemented
from solution import tokenize


############################################ Parsing


def parse(tokens):
    """
    If tokens is a list of tokens from a symbolic algebra expression,
    returns Expr representing the whole expression.

    >>> parse(['x'])
    Var('x')
    >>> parse(['15'])
    Num(15)
    >>> parse(['(', 'y', '+', 'z', ')'])
    Add(Var('y'),Var('z'))
    """

    def parse_expression(index):
        """
        Returns (expression, next_index)
        """
        pass

    parsed_expression, next_index = parse_expression(0)
    return parsed_expression


if __name__ == "__main__":
    import doctest

    doctest.testmod()
