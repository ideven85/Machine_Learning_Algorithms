# 6.101 recitation: LISP part 1, Scheme functions & environments

foo = lambda x: x**3


def deriv(f, dx):
    def fprime(x):
        return (f(x + dx) - f(x)) / dx

    return fprime


dfoo = deriv(foo, 0.001)
num = dfoo(2)
print(num)  # => 12.006000999997823

# (begin
#     (define foo (lambda (x) (* x x x)))
#     (define (deriv f dx)
#         (define (fprime x)
#             (/ (- (f (+ x dx)) (f x)) dx)))
#     (define dfoo (deriv foo .001))
#     (define num (dfoo 2))
#     (display num)
# )


(5 + 4) / (7 - 3 - 2 - 1) / 2  # => 4.5


(lambda x: x * x)(4)  # => 16


def area(r):
    return 3.14 * r**2


x = area(5)
y = x
print(y)  # => 78.5


def four():
    return 2 + 2


four()


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
