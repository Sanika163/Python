# 1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

# Example Input:

# [1000000,2000000,3000000,4000000]

# Expected Output

# [333333833333500000,2666668666667000000,...]

import multiprocessing 
import time
import os

def sumOfSquare(No):

    print(f"Process is running with PID : {os.getpid()}")

    sum = 0

    for i in range(1, No+1):
        sum = sum + (i**2)

    return sum

def main():
    Data = [1000000,2000000,3000000,4000000]
    Result =[]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(sumOfSquare, Data)

    pobj.close()
    pobj.join()

    print(f"Result is : {Result}")

    end_time = time.perf_counter()

    print(f"Time required : {end_time-start_time:.4f} seconds")

if __name__ == "__main__":
    main()