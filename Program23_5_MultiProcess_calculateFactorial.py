# 5: Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.

# Input: Data [10, 15, 20, 25]

# Expected Task
# For every N, calculate: N!

# Expected Output Format
# Process ID: 1240
# Input Number: 20
# Factorial 2432902008176640000

import multiprocessing
import time 
import os

def Factorial(No):
    
    PID = os.getpid()
    fact = 1

    for i in range(1, No+1):    
        fact = fact * i
    
    return PID, fact

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

    Result = pobj.map(Factorial, Numbers)

    pobj.close()
    pobj.join()

    print("Result is : ")

    for No, (PID, Ret) in zip(Numbers, Result):
        print(f"Factorial of {No} having PID {PID} is : {Ret}")
    
    end_time = time.perf_counter()

    print(f"Total time required : {end_time-start_time:.4f} seconds")

if __name__=="__main__":
    main()

