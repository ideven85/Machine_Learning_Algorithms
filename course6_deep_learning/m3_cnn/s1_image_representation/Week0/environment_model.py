functions = []
for i in range(5):

    def inner(func):
        return func + i

    functions.append(inner)

for f in functions:
    print(f(12))


def sum_lists(l):
    total = 0
    for x in l:
        total += sum(x)
    return total


inp = [[0, 1], [1, 2]]
print(sum_lists(inp))
