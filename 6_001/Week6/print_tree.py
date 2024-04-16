import time

tree1 = [13, [7], [8, [99], [16, [77]], [42]]]


def all_values(tree):
    if not tree:
        return

    parent = tree[0]
    children = tree[1:]
    if not children:
        return parent
    if len(children) == 1:
        yield parent, children[0]

    elif isinstance(children[0], list):
        yield from all_values(children[0])
        yield from all_values(children[1:])
    else:

        yield children[0]
        yield from all_values(children[1:])


print(list(all_values(tree1)))

out = []


def fib_gen(n):
    a = 0
    b = 1
    for i in range(n):
        yield b
        b += a
        a = b - a


x1 = fib_gen(1000)
s1 = time.time_ns()
for val in x1:
    out.append(val)
s2 = time.time_ns()

print(s2 - s1)

# print(out)


def fib(n):
    a = 0
    b = 1
    out1 = []
    for i in range(n):
        out1.append(b)
        b += a
        a = b - a

    return out1


s3 = time.time_ns()
a = fib(1000)
s4 = time.time_ns()
print(s4 - s3)
print(a[:5])
print(out[:5])
