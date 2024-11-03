def double_func(func):
    def inner(x):  # x is passed by the target function to the decorated function
        print(x)
        return 2 * func(x)

    return inner


@double_func
def half_of_x(x):

    print(x)
    return x


print(half_of_x(10))  # 20
print(double_func(half_of_x)(10))  # 40
