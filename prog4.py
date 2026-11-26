import threading
import time

BUFFER_SIZE = 5
ITEMS = 10

buffer = []
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)


def producer():
    for item in range(1, ITEMS + 1):
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        slot = (len(buffer) - 1) % BUFFER_SIZE
        print(f"Producer produced item {item} at slot {slot}")
        mutex.release()
        full.release()
        time.sleep(0.1)


def consumer():
    for _ in range(ITEMS):
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        print(f"\t\tConsumer consumed item {item}")
        mutex.release()
        empty.release()
        time.sleep(0.15)


p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()

p.join()
c.join()

print("All items produced and consumed.")