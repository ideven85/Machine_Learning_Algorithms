# 6.101 recitation: LISP part 1 wrap-up

#################################
# From Python to Scheme
#################################

a = 1
b = -5
c = 6

d = b * b - 4 * a * c


def square(x):
    return x * x


def f():
    return 42


#################################
# Evaluation
#################################

# in> ((lambda (x) (* x 3)) 5)
#   out> 15
# What expressions are evaluated? In what frames?
