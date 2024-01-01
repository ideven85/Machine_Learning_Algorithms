import time
import datetime


def factorial(n):
    return 1 if n <2 else n * factorial(n-1)

a=int(round(time.time()))
first=datetime.datetime.now().microsecond
list(factorial(i) for i in range(100))
second=datetime.datetime.now().microsecond
print(second,first,second-first)
print(int(round(time.time())-a))