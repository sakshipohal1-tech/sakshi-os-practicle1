import threading

NUM_THREADS = 4

class PartialSum:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0

def sum_array(p):
    p.sum = sum(range(p.start, p.end))
    tid = threading.get_ident() % 100000
    print(f"Thread {tid}: sum[{p.start}..{p.end}) = {p.sum}")

def main():
    n = 1000000
    chunk = n // NUM_THREADS
    threads = []
    data = []
    total = 0

    for i in range(NUM_THREADS):
        start = i * chunk
        end = n if i == NUM_THREADS - 1 else (i + 1) * chunk
        p = PartialSum(start, end)
        data.append(p)
        t = threading.Thread(target=sum_array, args=(p,))
        threads.append(t)
        t.start()

    for i in range(NUM_THREADS):
        threads[i].join()
        total += data[i].sum

    print(f"Total sum (0 to {n - 1}) computed using {NUM_THREADS} threads = {total}")

if __name__ == "__main__":
    main()