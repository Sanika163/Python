#2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().

#Input: [10,15,20,25]

#Display

# 1.Process ID

# 2.Input Number

# 3.Factorial

import multiprocessing
import time
import os

def Factorial(No):
    print(f"Process is running with PID : {os.getpid()}")

    fact = 1

    for i in range(1, No+1):
        fact = fact * i

    return fact


def main():
    N = int(input("Enter how many numbers you want to enter : "))
    Numbers = []

    Result = []

    for i in range(N):
        No = int(input())
        Numbers.append(No)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial, Numbers)

    pobj.close()
    pobj.join()

    print(f"Input Numbers are : {Numbers}")
    print(f"Result is : {Result}")

    end_time = time.perf_counter()

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()