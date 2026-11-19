# 3: Design a Python application where multiple threads update a shared variable.

# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

import time
import threading

counter = 0
lock = threading.Lock()

def incrementCounter(N):

    global counter

    for i in range(N):
        with lock:
            counter = counter + 1

def main():

    global counter

    N = int(input("Enter how many threads you want: "))
    M = int(input("Enter how many times each thread should increment: "))

    start_time = time.perf_counter()

    Threads = []

    for i in range(N):
        t = threading.Thread(
            target=incrementCounter,
            args=(M,),
            name=f"Thread{i+1}"
        )
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

    print("Final value of Counter:", counter)

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")
    print("Exit from Main")

if __name__ == "__main__":
    main()
