
# write a function to sum two numbers

def add(a,b):
    return a+b

# Write a function to find the factorial of n

def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

print(factorial(20))

# write a function to connect to postgresql

def factorialV2(n):
    i=1
    for x in range(1,n+1):
        i*=x
    return i

print(factorialV2(20))
def x(n):
    def inner(x):
        return x+n
    return inner

y = x(2)
print(y(2))
# write a function to  find the sum of all numbers between two numbers


def sum_of_numbers(a,b):
    s=0
    for x in range(a,b+1):
        s+=x
    return s

print(sum_of_numbers(2,5))

# write a function to find the largest number between two numbers

def max_number(a,b):
    return max(a,b)



    

