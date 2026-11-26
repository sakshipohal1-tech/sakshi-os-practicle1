MAXBLOCKS = 30

def contiguous_allocation():
    disk = [0] * MAXBLOCKS
    print("\n--- Contiguous Allocation ---")
    nf = int(input("Enter number of files: "))

    for f in range(nf):
        start, length = map(int, input(f"File {f + 1} - starting block, length: ").split())

        if start < 0 or start + length > MAXBLOCKS or any(disk[i] == 1 for i in range(start, start + length)):
            print("Allocation failed: blocks not free/out of range.")
            continue

        for i in range(start, start + length):
            disk[i] = 1
        print(f"File {f + 1} allocated blocks {start} to {start + length - 1}")

def linked_allocation():
    disk = [0] * MAXBLOCKS
    print("\n--- Linked Allocation ---")
    nf = int(input("Enter number of files: "))

    for f in range(nf):
        length = int(input(f"File {f + 1} - number of blocks: "))
        allocated = []

        for i in range(MAXBLOCKS):
            if len(allocated) == length:
                break
            if disk[i] == 0:
                disk[i] = 1
                allocated.append(str(i))

        chain = " -> ".join(allocated) + (" -> (NULL)" if allocated else "(NULL)")
        print(f"File {f + 1} allocated blocks: {chain}")
        if len(allocated) < length:
            print("Warning: disk full, could not allocate all blocks.")

def indexed_allocation():
    disk = [0] * MAXBLOCKS
    print("\n--- Indexed Allocation ---")
    nf = int(input("Enter number of files: "))

    for f in range(nf):
        length = int(input(f"File {f + 1} - number of data blocks needed: "))

        index_block = -1
        for i in range(MAXBLOCKS):
            if disk[i] == 0:
                index_block = i
                disk[i] = 1
                break

        data_blocks = []
        for i in range(MAXBLOCKS):
            if len(data_blocks) == length:
                break
            if disk[i] == 0:
                disk[i] = 1
                data_blocks.append(str(i))

        print(f"File {f + 1} - Index block: {index_block}, Data blocks: {' '.join(data_blocks)}")

def main():
    print("Menu:\n1. Contiguous Allocation\n2. Linked Allocation")
    choice = int(input("3. Indexed Allocation\nEnter choice: "))

    if choice == 1:
        contiguous_allocation()
    elif choice == 2:
        linked_allocation()
    elif choice == 3:
        indexed_allocation()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()