import threading
import time

N = 5

forks = [threading.Semaphore(1) for _ in range(N)]
room = threading.Semaphore(N - 1)  # Allows at most N-1 philosophers to pick up forks

def philosopher(philo_id):
    left = philo_id
    right = (philo_id + 1) % N

    for _ in range(2):
        print(f"Philosopher {philo_id} is thinking")
        time.sleep(0.1)

        room.acquire()          # Enter the "room" - avoids deadlock
        forks[left].acquire()   # Pick up left fork
        forks[right].acquire()  # Pick up right fork

        print(f"Philosopher {philo_id} is eating (fork {left} and fork {right})")
        time.sleep(0.15)

        forks[right].release()
        forks[left].release()
        room.release()

        print(f"Philosopher {philo_id} finished eating and put down forks")

def main():
    philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]

    for p in philosophers:
        p.start()
    for p in philosophers:
        p.join()

if __name__ == "__main__":
    main()