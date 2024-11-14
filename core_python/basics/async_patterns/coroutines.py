def simple():
    print("Co Routine Started")
    x = yield
    print("Co Routine Received", x)
    yield None


from pathlib import Path

a = simple()
next(a)
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)


def fib():

    term1 = 1
    term2 = 0
    total = 0
    out = None
    while True:
        yield term2
        term1 = term1 + term2

        term2 = term1 - term2


def calc_average():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


fibonacci = fib()
next(fibonacci)
for i in range(10):
    if i >= 5:
        fibonacci.close()
        break
    print(fibonacci.send(i))

a.send(20)
averager = calc_average()
next(averager)
print(averager.send(10))
print(averager.send(20))


a.close()
averager.close()
