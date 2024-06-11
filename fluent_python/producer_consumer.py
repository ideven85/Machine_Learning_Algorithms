import asyncio


async def main():
    await asyncio.sleep(1)
    print("hello")

# function to add two numnbers
def add(a, b):
    return a + b


    
def test_add():
    assert add(3, 5) == 8
    assert add(-3, 5) == 2
    assert add(-3, -5) == -8

# function to multiply two numbers
def mul(a,b):
    return a*b


