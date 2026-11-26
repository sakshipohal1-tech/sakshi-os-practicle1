def first_fit(bsize, psize):
    bn, pn = len(bsize), len(psize)
    block = bsize[:]
    allocation = [-1] * pn

    for i in range(pn):
        for j in range(bn):
            if block[j] >= psize[i]:
                allocation[i] = j
                block[j] -= psize[i]
                break

    print("\n--- First Fit ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(pn):
        blk = f"B{allocation[i] + 1}" if allocation[i] != -1 else "Not Allocated"
        print(f"P{i + 1}\t\t{psize[i]}\t\t{blk}")

def best_fit(bsize, psize):
    bn, pn = len(bsize), len(psize)
    block = bsize[:]
    allocation = [-1] * pn

    for i in range(pn):
        best_idx = -1
        for j in range(bn):
            if block[j] >= psize[i]:
                if best_idx == -1 or block[j] < block[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            block[best_idx] -= psize[i]

    print("\n--- Best Fit ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(pn):
        blk = f"B{allocation[i] + 1}" if allocation[i] != -1 else "Not Allocated"
        print(f"P{i + 1}\t\t{psize[i]}\t\t{blk}")

def worst_fit(bsize, psize):
    bn, pn = len(bsize), len(psize)
    block = bsize[:]
    allocation = [-1] * pn

    for i in range(pn):
        worst_idx = -1
        for j in range(bn):
            if block[j] >= psize[i]:
                if worst_idx == -1 or block[j] > block[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            block[worst_idx] -= psize[i]

    print("\n--- Worst Fit ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(pn):
        blk = f"B{allocation[i] + 1}" if allocation[i] != -1 else "Not Allocated"
        print(f"P{i + 1}\t\t{psize[i]}\t\t{blk}")

def main():
    bn = int(input("Enter number of memory blocks: "))
    bsize = list(map(int, input("Enter sizes of blocks: ").split()))[:bn]

    pn = int(input("Enter number of processes: "))
    psize = list(map(int, input("Enter sizes of processes: ").split()))[:pn]

    first_fit(bsize, psize)
    best_fit(bsize, psize)
    worst_fit(bsize, psize)

if __name__ == "__main__":
    main()