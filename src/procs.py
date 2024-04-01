import asyncio
import math


async def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    mid = math.isqrt(n)
    for i in range(3,mid+1,2):
        if n%i==0:
            return False
        if i%1_000_000==0:
            await asyncio.sleep(0)
    return True

print(is_prime(1234567890))