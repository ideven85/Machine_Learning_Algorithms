x = 0
def outer():
    # x = 1
    def inner():
        # x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

x = 3
outer()
print("global:", x)

"""
Question 3 -- What will the code above output?
"""