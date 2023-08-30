import math
import os
import time
from multiprocessing import Process

def calc():
    for i in range(1,70000000000):
        time.sleep(1)
        print(math.sqrt(i),end=' ')
processes = []

for i in range(os.cpu_count()):
    print('Registering Process: %d' %i)
    processes.append(Process(target=calc))

for p in processes:
    p.start()
for p in processes:
    p.join()

