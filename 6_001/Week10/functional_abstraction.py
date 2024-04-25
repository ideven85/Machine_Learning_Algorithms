class Memoised_Function:
    def __init__(self,func):
        self.func=func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args]=self.func(*args)
        return self.cache[args]

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)

f=Memoised_Function(fib)
print(f(40))