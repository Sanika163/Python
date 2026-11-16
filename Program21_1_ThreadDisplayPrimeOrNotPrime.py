# 1: Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import time
import math
import threading

def is_Prime(No):
    if No < 2:
        return False
    
    for i in range(2, (math.isqrt(No)) + 1):
        if No % i == 0:
            return False
        
    return True

def checkPrime(Numbers):
    prime = [number for number in Numbers if is_Prime(number)]
    print(f"List of Prime Numbers : {prime}")


def checkNonPrime(Numbers):
    NonPrime = [number for number in Numbers if not is_Prime(number)]
    print(f"List of Non Prime Numbers : {NonPrime}")

def main():

    N = int(input("Enter how many numbers you want :"))

    Numbers = []

    for i in range(N):
        Num = int(input())
        Numbers.append(Num)

    start_time = time.perf_counter()

    checkPrime_Thread = threading.Thread(target=checkPrime, args=(Numbers, ))
    checkNonPrime_Thread = threading.Thread(target=checkNonPrime, args=(Numbers,))
    
    checkPrime_Thread.start()
    checkNonPrime_Thread.start()

    checkPrime_Thread.join()
    checkNonPrime_Thread.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")
    
if __name__=="__main__":
    main()