import main
import time
s1 = time.perf_counter()
print(main.prime_list(40000))
s2 = time.perf_counter()
print(main.prime_number_optimised(400000000))
s3 = time.perf_counter()
print(s2-s1)
print(s3-s2)