# 4: Write a program that counts how many odd numbers exist between 1 and N.

# Input: Data [1000000, 2000000, 3000000, 4000000]

# Expected Output Format
# Process ID: 1237
# Input Number: 1000000
# Odd Number Count: 500000

import multiprocessing
import time 
import os

def countOddNumbers(No):
    
    PID = os.getpid()
    count = 0

    for i in range(1, No+1, 2):    
        count = count + 1
    
    return PID, count

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

    Result = pobj.map(countOddNumbers, Numbers)

    pobj.close()
    pobj.join()

    print("Result is : ")

    for No, (PID, Ret) in zip(Numbers, Result):
        print(f"Count of Odd Numbers for {No} having PID {PID} is : {Ret}")
    
    end_time = time.perf_counter()

    print(f"Total time required : {end_time-start_time:.4f} seconds")

if __name__=="__main__":
    main()

