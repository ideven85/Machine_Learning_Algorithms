"""
Question 2: What if we wanted to be able to make expressions without
having to wrap every operation in parentheses?

For now, we'll assume that expression now takes in a well-formed string of
tokens in one of the following forms:
- single number
- single variable
- one or more symbols surrounded by parentheses, with an
operator of equal precedence separating each symbol.
Examples:
expression('(x)') -> Var('x')
expression('(1 + 2 + 3)') -> Add(Add(Num(1), Num(2)), Num(3))
expression('(-1 - -2 + 3)') -> Add(Sub(Num(-1), Num(-2)), Num(3))
expression('(-1 - (-2 / x * 5) + 3)') -> Add(Sub(Num(-1), Mul(Div(Num(-2), Var('x')), Num(3))

Implement parse below to parse these new kinds of expressions!

Question 3: Error-catching
What should we do if the expression is not well-formed? Instead
of letting Python handle the exception, we are going to try to
cleanly raise a custom exception called a SymbolSyntaxError.

Before running / looking at the examples in test_error_expression(),
list different ways an expression could be malformed. Make a plan for
how you could detect various errors (preferably without using try/except)
before you start implementing code.

Note: you will need to copy your lab.py file into this folder
in order to get the tests to pass.
"""

from lab import *
from test import symbol_rep



def parse(tokens):  # tokens is a list of strings
    pass



class SymbolSyntaxError(Exception):
    """
    Exception to be raised when trying to parse a malformed expression.
    """
    pass


def expression(inp):
    return parse(tokenize(inp))


def test_long_expression():
    result = expression('(x)')
    expected = Var('x')
    assert symbol_rep(result) == symbol_rep(expected), f'{repr(result)}  != {repr(expected)}'

    result = expression('(1 + 2 + 3)')
    expected = Add(Add(Num(1), Num(2)), Num(3))
    assert symbol_rep(result) == symbol_rep(expected), f'{repr(result)}  != {repr(expected)}'
    assert result.eval({}) == 6

    result = expression('(-1 - -2 + 3)')
    expected = Add(Sub(Num(-1), Num(-2)), Num(3))
    assert symbol_rep(result) == symbol_rep(expected), f'{repr(result)}  != {repr(expected)}'
    assert result.eval({}) == 4

    result = expression('(-1 - (-2 / x * 5) + 3)')
    expected = Add( Sub(Num(-1), Mul(Div(Num(-2), Var('x')), Num(5))), Num(3))
    assert symbol_rep(result) == symbol_rep(expected), f'{repr(result)}  != {repr(expected)}'
    assert result.eval({"x": 2}) == 7

    print("expression works as expected!")


def test_error_expression():
    try:
        result = expression("(x x)")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'

    result = expression("(x)")
    assert result == Var('x')


    try:
        result = expression("(x + 3 * 8)")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'


    try:
        result = expression("(x")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'

    try:
        result = expression("(x +")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'


    try:
        result = expression("(x + x")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'

    try:
        result = expression("(x + x))")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'

    try:
        result = expression("((x + x)")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'

    try:
        result = expression("(x - x")
        assert False, "No error raised!"
    except SymbolSyntaxError:
        assert True, "Yay!"
    except Exception as e:
        assert False, f'Wrong error raised! {e}'


if __name__ == "__main__":
    test_long_expression()
    test_error_expression()
    print("done!")