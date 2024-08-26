x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

"""
Question 2 -- What will the code above output?
Draw an environment diagram to represent the program execution.
"""