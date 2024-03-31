import time
from threading import Thread


def factorial(n):
    s=1
    for i in range(1,n):
        s*=i

    print(f'Done factorial:{n}={s}')



if __name__ == '__main__':
    threads = [Thread(target=factorial,args=(i,)) for i in range(2,100)]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print(end-start)