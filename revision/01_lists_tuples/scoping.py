fns = []
for i in range(5):

    def func(x):
        return x + i

    fns.append(func)

for f in fns:
    print(f(12), i)  # if you use i here it is still in play with value 4
