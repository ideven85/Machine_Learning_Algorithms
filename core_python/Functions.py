x = 100

def foo(y):
    return x+y

z = foo(307)
print(x,z,foo)
def bar(x):
    x=1000
    return foo(308)
w=bar(349)
print(x,w)

def apply_n_times(f,n,x):
    out = x
    for i in range(n):
        out=f(out)

    return out

def double(x):
    return x*2

print(apply_n_times(double,3,3)) # 12


"""
Decorators and Closures
"""
def decorate(func):
    def inner():
        return func
    return inner

@decorate
def target():
    return "target"
def variable_length_arguments(*args,**kwargs):
    """Function to describe Variable length features of variable with * and ** operators.Variable is passed as reference"""
    print("*Args is a tuple:")
    #args[0] = "Khan"
    for arg in args:
        print(arg,end=' ')
    print(args)
    for key,value in kwargs.items():
        print(key,value)
    print("\n*Kwargs is a dictionary")


summing = lambda x:x+x

def compute_squares(numbers):
    """
    Object is passed by reference

    """
    numbers[0]=11
    numbers.sort() # No Reassignment
    return sorted(i*i for i in numbers)

def swap(x,y):
    x=x+y
    y = x-y
    x=x-y
    return x,y




if __name__ == '__main__':
    l = ['Hi','I','am','an','example']
    dictionary = dict(first='Geeks',mid='For',last='Geeks')
    print(variable_length_arguments.__doc__)

    variable_length_arguments(l,dictionary)
    l = list(range(1,10))
    print(summing(l))
    print(l)
    print(compute_squares(l))
    print(l)
    print(compute_squares.__doc__)
    x=10;y=20
    x,y=swap(x,y)
    print(x,y)
