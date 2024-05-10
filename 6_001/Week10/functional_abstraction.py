class Memoized_Function:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# f = Memoized_Function(fib)
# print(f.__call__(2))
# print(f(40))
# f1 = fib(2)

def words_upper(words):
    return [w.upper() for w in words]


def words_list_upper(words):
    if len(words) == 1:
        return [words[0].upper()]
    return sorted([words[0].upper()] + words_list_upper(words[1:]))


a = ["abc", "ghi", "def"]

print(words_list_upper(a))
