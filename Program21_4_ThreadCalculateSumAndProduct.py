# 4: Design a Python application that creates two threads.

# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import time
import math
import threading

def calculateSum(Numbers, Result):
    sum = 0

    for No in Numbers:
        sum = sum + No

    Result[0] =  sum

def calculateProduct(Numbers, Result):
    product = 1

    for No in Numbers:
        product = product * No

    Result[1] =  product

def main():

    N = int(input("Enter how many numbers you want :"))

    Numbers = []

    Result = [0, 0]

    for i in range(N):
        Num = int(input())
        Numbers.append(Num)

    start_time = time.perf_counter()

    checkPrime_Thread = threading.Thread(target=calculateSum, args=(Numbers, Result))
    checkNonPrime_Thread = threading.Thread(target=calculateProduct, args=(Numbers, Result))
    
    checkPrime_Thread.start()
    checkNonPrime_Thread.start()

    checkPrime_Thread.join()
    checkNonPrime_Thread.join()

    print(f"Sum of Elements from list is : {Result[0]}")
    print(f"Product of Elements from list is : {Result[1]}")
    
    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")
    
if __name__=="__main__":
    main()