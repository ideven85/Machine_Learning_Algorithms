import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤$%^^&*^%$##'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))
def non_ascii(c):
    return c>127 # Closure
def simple_function(symbols):
    output = []
    for symbol in symbols:
        if ord(symbol)>127:
            output.append(symbol)
    return output

clock('simple_function', 'simple_function')

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
