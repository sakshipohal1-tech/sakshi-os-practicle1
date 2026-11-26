def fifo(pages, nf):
    frames = []
    faults = 0
    pointer = 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < nf:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % nf
    print(f"FIFO Page Faults = {faults}")


def lru(pages, nf):
    frames = []
    last_used = {}
    faults = 0
    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < nf:
                frames.append(page)
            else:
                victim = min(frames, key=lambda p: last_used[p])
                frames[frames.index(victim)] = page
        last_used[page] = i
    print(f"LRU Page Faults = {faults}")


def optimal(pages, nf):
    frames = []
    faults = 0
    for i, page in enumerate(pages):
        if page in frames:
            continue
        faults += 1
        if len(frames) < nf:
            frames.append(page)
        else:
            future = pages[i + 1:]
            distances = [future.index(p) if p in future else float('inf') for p in frames]
            frames[distances.index(max(distances))] = page
    print(f"Optimal Page Faults = {faults}")


n = int(input("Enter number of pages in reference string: "))
pages = list(map(int, input("Enter the reference string: ").split()))
f = int(input("Enter number of frames: "))

fifo(pages, f)
lru(pages, f)
optimal(pages, f)