import math
import os
import time
from threading import Thread

def calc():
    for i in range(1,4000000):
        time.sleep(1)
        print(math.sqrt(i),end=' ')

threads = []

for i in range(os.cpu_count()):
    print('Registering Thread: %d' %i)
    threads.append(Thread(target=calc))

for t in threads:
    t.start()

for t in threads:
    t.join()
