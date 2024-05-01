import copy
import time
from itertools import permutations
out = []
def find_permutations_with_list(s:str):


    list_permutations("",s)
    return out

def list_permutations(prefix, curr):
        n = len(curr)
        if n == 0:
            out.append(prefix)
        for i in range(n):
            list_permutations(prefix + curr[i], curr[i + 1:] + curr[:i])

def find_permutations(s):
    a=generate_permutations("",s)
    return a
def generate_permutations(prefix, curr):
        n = len(curr)
        if n == 0:
            yield prefix
        for i in range(n):
            yield from generate_permutations(prefix + curr[i], curr[i + 1:] + curr[:i])

print("Using new learnt syntax")
start=time.perf_counter()
out1=find_permutations("ABCDEFGH")
end=time.perf_counter()
print(end-start) # 5.829997462569736e-07
print(list(out1)[:5])
start=time.perf_counter()
x=find_permutations_with_list("ABCDEFGH")
end=time.perf_counter()
print(end-start) # 0.01884433299983357
print(x[:5])
print("Using In Built Function")
start=time.perf_counter()
x=permutations("ABC")
end=time.perf_counter()
print(end-start) # 1.7500005924375728e-06
print(list(x))

# With Yield 1.4792000001762062e-05
# With Append 1.6292000509565696e-05