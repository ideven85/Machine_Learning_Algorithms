import queue
import threading

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished working on {item}')
        q.task_done()

threading.Thread(target=worker,daemon=True,name="First").start()


for item in range(10):
    q.put(item)

q.join()
print("All work completed")