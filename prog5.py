import threading
import time

mutex = threading.Semaphore(1)
wrt = threading.Semaphore(1)
read_count = 0
shared_data = 0


def reader(i):
    global read_count
    mutex.acquire()
    read_count += 1
    if read_count == 1:
        wrt.acquire()
    mutex.release()

    print(f"Reader {i}: read shared_data = {shared_data}")
    time.sleep(0.2)

    mutex.acquire()
    read_count -= 1
    if read_count == 0:
        wrt.release()
    mutex.release()


def writer(i):
    global shared_data
    wrt.acquire()
    shared_data += 1
    print(f"Writer {i}: wrote shared_data = {shared_data}")
    time.sleep(0.3)
    wrt.release()


w1 = threading.Thread(target=writer, args=(1,))
r = [threading.Thread(target=reader, args=(i + 1,)) for i in range(5)]
w2 = threading.Thread(target=writer, args=(2,))

w1.start()
for t in r:
    t.start()
w2.start()

for t in r:
    t.join()
w1.join()
w2.join()