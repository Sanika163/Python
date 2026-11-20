# 4. Write a program that calculates

# 1^5+2^5+3^5+.....+N^5 for multiple values of N simultaneously using Pool.

# Input: [1000000, 2000000, 3000000, 4000000]

# Measure total execution time.

import multiprocessing
import time
import os
import math

def sumOfPower5(No):
    print(f"Process is running with PID : {os.getpid()}")

    sum = 0

    for i in range(1, No+1):
        sum = sum + (i**5)

    return sum

def main():
    N = int(input("Enter how many numbers you want to enter : "))
    Numbers = []

    Result = []

    for i in range(N):
        No = int(input())
        Numbers.append(No)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(sumOfPower5, Numbers)

    pobj.close()
    pobj.join()

    print(f"Input Numbers are : {Numbers}")
    print(f"Result is : {Result}")

    end_time = time.perf_counter()

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()