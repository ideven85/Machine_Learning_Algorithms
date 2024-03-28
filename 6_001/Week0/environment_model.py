functions = []
for i in range(5):

    def inner(func):
        return func + i

    functions.append(inner)

for f in functions:
    print(f(12))

def sum_lists(l):
    output = [0]*(len(l))
    for i in range(len(l)):
        total = 0
        for i in l[i]:
            total += i
        output[i]=total
    return output

inp = [[0,1],[1,2]]
print(sum_lists(inp))