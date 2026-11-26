P = 5
R = 3

available = list(map(int, input("Enter available resources of each type (3 types): ").split()))
print("Enter Maximum matrix (5 processes x 3 resources):")
maximum = [list(map(int, input().split())) for _ in range(P)]
print("Enter Allocation matrix:")
allocation = [list(map(int, input().split())) for _ in range(P)]

need = [[maximum[i][j] - allocation[i][j] for j in range(R)] for i in range(P)]


def safe_state():
    work = available[:]
    finish = [False] * P
    sequence = []

    while len(sequence) < P:
        found = False
        for i in range(P):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(R)):
                work = [work[j] + allocation[i][j] for j in range(R)]
                finish[i] = True
                sequence.append(i)
                found = True
        if not found:
            return None
    return sequence


seq = safe_state()
if seq:
    print("System is in a SAFE state.")
    print("Safe sequence:", " -> ".join(f"P{i}" for i in seq))
else:
    print("System is in an UNSAFE state.")

pid = int(input("\nEnter process number requesting resources (0-4): "))
request = list(map(int, input("Enter request vector (3 values): ").split()))

if any(request[j] > need[pid][j] for j in range(R)):
    print("Error: process has exceeded its maximum claim.")
elif any(request[j] > available[j] for j in range(R)):
    print("Error: resources are not available.")
else:
    for j in range(R):
        available[j] -= request[j]
        allocation[pid][j] += request[j]
        need[pid][j] -= request[j]

    if safe_state():
        print("Request can be granted safely.")
    else:
        for j in range(R):
            available[j] += request[j]
            allocation[pid][j] -= request[j]
            need[pid][j] += request[j]
        print("Request denied: would lead to an unsafe state.")