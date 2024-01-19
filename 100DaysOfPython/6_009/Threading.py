"""
Single Threading Example
"""
import math
import time
from threading import Thread


class MyThread:
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print('Boil Milk for 1 second and powder for 5 minutes',end=' ')
        time.sleep(5)
        print('Done')

    def task2(self):
        print('Add sugar for 1 second and powder for 5 minutes', end=' ')
        time.sleep(5)
        print('Done')
    def task3(self):
        print('Filter it and done', end=' ')
        time.sleep(5)
        file=open('file1.txt','w')
        file.write('I want to see a movie. A porn slutty movie')
        file.close()
        print('Done')


def sqrt(x):
    if not isinstance(x,int):
        raise TypeError('Bitch give a number')
    if x<0:
        raise ValueError('x must be greater than 0')
    else:
        return math.sqrt(x)

obj = MyThread()
t = Thread(target=obj.prepareTea)
t.start()