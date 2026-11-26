def fcfs(req, head):
    total = 0
    cur = head
    for r in req:
        total += abs(cur - r)
        cur = r
    print(f"FCFS   total head movement = {total}")

def sstf(req, head):
    n = len(req)
    visited = [False] * n
    total = 0
    cur = head

    for _ in range(n):
        idx = -1
        best = float("inf")
        for i in range(n):
            if not visited[i] and abs(cur - req[i]) < best:
                best = abs(cur - req[i])
                idx = i
        visited[idx] = True
        total += best
        cur = req[idx]

    print(f"SSTF   total head movement = {total}")

def scan(req, head, disk_size):
    arr = sorted(req + [head])
    idx = arr.index(head)

    total = 0
    cur = head
    # Go towards the higher end first
    for i in range(idx + 1, len(arr)):
        total += abs(cur - arr[i])
        cur = arr[i]
    total += abs(cur - (disk_size - 1))
    cur = disk_size - 1
    for i in range(idx - 1, -1, -1):
        total += abs(cur - arr[i])
        cur = arr[i]

    print(f"SCAN   total head movement = {total}")

def cscan(req, head, disk_size):
    arr = sorted(req + [head])
    idx = arr.index(head)

    total = 0
    cur = head
    for i in range(idx + 1, len(arr)):
        total += abs(cur - arr[i])
        cur = arr[i]
    total += abs(cur - (disk_size - 1))  # Go to the end
    total += (disk_size - 1)             # Jump to cylinder 0
    cur = 0
    for i in range(0, idx):
        total += abs(cur - arr[i])
        cur = arr[i]

    print(f"C-SCAN total head movement = {total}")

def main():
    n = int(input("Enter number of requests: "))
    req = list(map(int, input("Enter the requests: ").split()))[:n]
    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size (max cylinder + 1): "))

    fcfs(req, head)
    sstf(req, head)
    scan(req, head, disk_size)
    cscan(req, head, disk_size)

if __name__ == "__main__":
    main()