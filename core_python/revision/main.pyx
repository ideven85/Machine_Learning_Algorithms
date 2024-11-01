#cython: language_level=3

import sys
sys.setrecursionlimit(100000000)
sys.set_int_max_str_digits(1000000)
def prime_list(total):
    number=2
    primes = []
    while number<total:
        for x in primes:
            if number%x==0:
                break
        else:
            primes.append(number)
        number+=1
    return primes

def prime_number_optimised(int amount):
    cdef int number,x, found
    cdef int primes[100000]

    amount=min(100000,amount)

    found=0
    number=2
    while number<amount:
        for x in primes[:found]:
            if number%x==0:
                break
        else:
            primes[found]=number
            found+=1
        number+=1
    answer = [p for p in primes[:found]]
    return answer


def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

def factorial_optimal(long n)->str:
    if n<=1:
        return "1"
    else:
        a=0;b=1
        for i in range(n):
            b+=a
            a=b-a
        return str(b)
