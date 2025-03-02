import multiprocessing

def fib(n):
    return n if n<2 else fib(n-1)+fib(n-2)

def main():
    for _ in range(multiprocessing.cpu_count()):
        multiprocessing.Process(target=fib,args=(35,)).start()

if __name__ == '__main__':
    main()