def list_range(start, stop, step=1):
    assert step >= 1
    out = []
    current = start
    while current < stop:
        out.append(current)
        current += step
    # print("Out",out)
    return out  # Out goes until the end of range


def gen_range(start, stop, step=1):  # Using Generators
    assert step >= 1
    current = start
    while current < stop:  # Loop Stops at the condition
        yield current
        current += step


for i in gen_range(0, 1_000, step=1):
    if i > 100:
        break
    print(i**2)

for i in list_range(0, 1_000):
    if i > 100:
        break
    print(i**2)


def gen1():
    yield 1
    yield 2


def gen2():
    yield 8
    yield 9


def get_generators():
    yield from gen1()
    yield from gen2()


for val in get_generators():
    print(val, end=" ")
print()


def negate_elements(x):
    for val in x:
        yield -val


a = [1, 2, 3]
for val in negate_elements(a):
    print(val, end=" ")