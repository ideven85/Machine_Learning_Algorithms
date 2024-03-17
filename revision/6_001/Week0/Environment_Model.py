functions = []
for i in range(5):
    def inner(func):
        return func +i
    functions.append(inner)

for f in functions:
    print(f(12))