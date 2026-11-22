# 1: Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers from 1 to N for every number from the given list.

# Input: Data [1000000, 2000000, 3000000, 4000000]

# Expected Task
# For each number N, calculate:
# 2 + 4 + 6 + ... + N

# Expected Output Format
# Process ID: 1234
# Input Number: 1000000
# Sum of Even Numbers: 250000500000

import multiprocessing
import time 
import os

def sumOfNEvenNumbers(No):
    
    PID = os.getpid()
    sum = 0

    for i in range(2, No+1, 2):    
        sum = sum+i
    
    return PID, sum

def main():
    N = int(input("Enter Number of elements you want : "))

    Numbers = []
    Result = []

    print(f"Enter {N} Numbers : ")

    for i in range(N):
        No = int(input())
        Numbers.append(No)

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(sumOfNEvenNumbers, Numbers)

    pobj.close()
    pobj.join()

    print("Result is : ")

    for No, (PID, Ret) in zip(Numbers, Result):
        print(f"Sum of Even Numbers for {No} having PID {PID} is : {Ret}")
    
    end_time = time.perf_counter()

    print(f"Total time required : {end_time-start_time:.4f} seconds")

if __name__=="__main__":
    main()
