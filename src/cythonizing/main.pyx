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
