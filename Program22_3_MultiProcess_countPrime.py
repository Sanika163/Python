# 3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.

# Example: [10000 20000 30000 40000]
# Output : [168, 303, 430, 550]
# Display total prime count for each number.


import multiprocessing
import time
import os
import math

def countPrimeNumbers(No):
    print(f"Process is running with PID : {os.getpid()}")

    count = 0

    for i in range(2, No+1):
        isPrime = True
        for j in range(2, int(math.sqrt(i+1)) + 1):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            count = count + 1

    return count

def main():
    N = int(input("Enter how many numbers you want to enter : "))
    Numbers = []

    Result = []

    for i in range(N):
        No = int(input())
        Numbers.append(No)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(countPrimeNumbers, Numbers)

    pobj.close()
    pobj.join()

    print(f"Input Numbers are : {Numbers}")
    print(f"Result is : {Result}")

    end_time = time.perf_counter()

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()