from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from typing import Callable


@dataclass
class Process:
    pid: int
    at: int
    bt: int
    pr: int
    ct: int = 0
    tat: int = 0
    wt: int = 0
    rem: int = 0

    def __post_init__(self) -> None:
        self.rem = self.bt

    def finalize(self, completion_time: int) -> None:
        self.ct = completion_time
        self.tat = self.ct - self.at
        self.wt = self.tat - self.bt


def print_result(processes: list[Process]) -> None:
    if not processes:
        print("No processes to display.")
        return

    print(f"\n{'PID':<6}{'AT':<6}{'BT':<6}{'PR':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")
    print("-" * 42)
    for p in processes:
        print(f"{p.pid:<6}{p.at:<6}{p.bt:<6}{p.pr:<6}{p.ct:<6}{p.tat:<6}{p.wt:<6}")

    n = len(processes)
    avg_wt = sum(p.wt for p in processes) / n
    avg_tat = sum(p.tat for p in processes) / n
    print(f"\nAverage Waiting Time     = {avg_wt:.2f}")
    print(f"Average Turnaround Time  = {avg_tat:.2f}")


def fcfs(processes: list[Process]) -> list[Process]:
    procs = sorted(deepcopy(processes), key=lambda p: (p.at, p.pid))
    time = 0
    for p in procs:
        time = max(time, p.at) + p.bt
        p.finalize(time)
    return sorted(procs, key=lambda p: p.pid)


def _non_preemptive(
    processes: list[Process], key_fn: Callable[[Process], tuple]
) -> list[Process]:
    procs = deepcopy(processes)
    pending = list(procs)
    time = 0

    while pending:
        available = [p for p in pending if p.at <= time]
        if not available:
            time = min(p.at for p in pending)
            continue

        chosen = min(available, key=key_fn)
        time += chosen.bt
        chosen.finalize(time)
        pending.remove(chosen)

    return sorted(procs, key=lambda p: p.pid)


def sjf(processes: list[Process]) -> list[Process]:
    return _non_preemptive(processes, key_fn=lambda p: (p.bt, p.at, p.pid))


def priority_scheduling(processes: list[Process]) -> list[Process]:
    return _non_preemptive(processes, key_fn=lambda p: (p.pr, p.at, p.pid))


def round_robin(processes: list[Process], quantum: int) -> list[Process]:
    if quantum <= 0:
        raise ValueError("Time quantum must be greater than 0.")

    procs = sorted(deepcopy(processes), key=lambda p: (p.at, p.pid))
    ready: deque[Process] = deque()
    unarrived = deque(procs)
    time = 0

    while ready or unarrived:
        if not ready:
            time = max(time, unarrived[0].at)
            while unarrived and unarrived[0].at <= time:
                ready.append(unarrived.popleft())

        current = ready.popleft()
        slice_time = min(current.rem, quantum)
        time += slice_time
        current.rem -= slice_time

        while unarrived and unarrived[0].at <= time:
            ready.append(unarrived.popleft())

        if current.rem > 0:
            ready.append(current)
        else:
            current.finalize(time)

    return sorted(procs, key=lambda p: p.pid)


def main() -> None:
    n = int(input("Enter number of processes: "))
    processes = [
        Process(
            i + 1,
            *map(
                int,
                input(f"Process {i + 1} Arrival Time, Burst Time, Priority: ").split(),
            ),
        )
        for i in range(n)
    ]

    print("\nMenu:")
    print("1. FCFS")
    print("2. SJF (Non-preemptive)")
    print("3. Priority (Non-preemptive)")
    print("4. Round Robin")
    choice = int(input("Enter choice: "))

    algorithms: dict[int, Callable[[list[Process]], list[Process]]] = {
        1: fcfs,
        2: sjf,
        3: priority_scheduling,
    }

    if choice in algorithms:
        print_result(algorithms[choice](processes))
    elif choice == 4:
        quantum = int(input("Enter time quantum: "))
        print_result(round_robin(processes, quantum))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()