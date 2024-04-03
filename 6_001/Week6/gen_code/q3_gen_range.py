"""
Question 1:	What is an iterable? An iterator? A generator?
What are the similarities and differences between them?


Question 2: How do you make an iterator from an iterable object in Python?


Question 3: What will the following example code below output?
"""

def gen_range(start, stop, step=1):
    print("HI 1")
    assert step >= 1
    current = start
    while current < stop:
        print("HI 2")
        yield current
        print("HI 3")
        current += step

    print("HI 4")

print("Example 1:")
x = gen_range(10, 13)
y = x
print(x)

print("Example 2:")
print(next(x))

print("Example 3:")
print(next(y))
print(next(x))

print("Example 4:")
print(next(y))
print(next(x))

