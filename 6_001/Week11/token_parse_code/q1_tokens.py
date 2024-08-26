"""
Question 1: Implement the tokenize function below as a
generator. Then, implement parse to work with this new tokenize
function.

Note: you will need to copy your lab.py file into this folder
in order to get the tests to pass.
"""

from lab import *
from test import symbol_rep, read_expected

def tokenize(x):
    pass # implement me!

def parse(token_gen):
    def parse_helper():  # why is no argument needed?
        pass

    return parse_helper()


def expression(inp):
    return parse(tokenize(inp))


def test_tokenize_gen():
    import types
    inputs = ["x", "20", "6.1010", "-4.9", "(0 + x)",
              "(-101 * x)", "(x + (-.5 / x))",
              "(0 + x)", "(-101 * x)", "(y * -2)",
              "((z * 3) + 0)", "((7 * A) / 9)",
              "(z + (x + 1))", "(A - (x + A))",
              "(y / (x / z))","((x * y) * z)", "((x + A) * (y + z))"
    ]
    expected_outputs = [['x'], ['20'], ['6.1010'], ['-4.9'],
        ['(', '0', '+', 'x', ')'], ['(', '-101', '*', 'x', ')'],
        ['(', 'x', '+', '(', '-.5', '/', 'x', ')', ')'],
        ['(', '0', '+', 'x', ')'], ['(', '-101', '*', 'x', ')'],
        ['(', 'y', '*', '-2', ')'], ['(', '(', 'z', '*', '3', ')', '+', '0', ')'],
        ['(', '(', '7', '*', 'A', ')', '/', '9', ')'],
        ['(', 'z', '+', '(', 'x', '+', '1', ')', ')'],
        ['(', 'A', '-', '(', 'x', '+', 'A', ')', ')'],
        ['(', 'y', '/', '(', 'x', '/', 'z', ')', ')'],
        ['(', '(', 'x', '*', 'y', ')', '*', 'z', ')'],
        ['(', '(', 'x', '+', 'A', ')', '*', '(', 'y', '+', 'z', ')', ')']
    ]

    for inp, exp_list in zip(inputs, expected_outputs):
        tgen = tokenize(inp)
        assert isinstance(tgen, types.GeneratorType)
        res_list = list(tokenize(inp))
        assert res_list == exp_list, f'{res_list=} != {exp_list=}'
        assert next(tgen) == exp_list[0], f'First token does not match!'
        assert list(tgen) == exp_list[1:], f'Remaining tokens do not match!'
        assert list(tgen) == [], f'Generator not exhausted!'

    print("tokenize works as expected!")


def test_expression():
    result = expression("x")
    expected = Var("x")
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("20")
    expected = Num(20)
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("6.1010")
    expected = Num(6.1010)
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("-4.9")
    expected = Num(-4.9)
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("(0 + x)")
    expected = Add(Num(0), Var("x"))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("(-101 * x)")
    expected = Mul(Num(-101), Var("x"))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("(x + (-.5 / x))")
    expected = Add(Var("x"), Div(Num(-0.5), Var("x")))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("(y * -2)")
    expected = Mul(Var("y"), Num(-2))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("((z * 3) + 0)")
    expected = Add(Mul(Var("z"), Num(3)), Num(0))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("((7 * A) / 9)")
    expected = Div(Mul(Num(7), Var("A")), Num(9))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("(z + (x + 1))")
    expected = Add(Var("z"), Add(Var("x"), Num(1)))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("(A - (x + A))")
    expected = Sub(Var("A"), Add(Var("x"), Var("A")))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("(y / (x / z))")
    expected = Div(Var("y"), Div(Var("x"), Var("z")))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("((x * y) * z)")
    expected = Mul(Mul(Var("x"), Var("y")), Var("z"))
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression("((x + A) * (y + z))")
    expected = read_expected("187_out.pyobj")
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression(read_expected("188_in.pyobj"))
    expected = read_expected("188_out.pyobj")
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression(read_expected("189_in.pyobj"))
    expected = read_expected("189_out.pyobj")
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression(read_expected("190_in.pyobj"))
    expected = read_expected("190_out.pyobj")
    assert symbol_rep(result) == symbol_rep(expected)

    result = expression(read_expected("191_in.pyobj"))
    expected = read_expected("191_out.pyobj")
    assert symbol_rep(result) == symbol_rep(expected)

    print("expression works as expected!")

if __name__ == "__main__":
    test_tokenize_gen()
    test_expression()