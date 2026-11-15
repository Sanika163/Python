# 1: Design a Python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import time
import threading

def displayEvenNumbers():

    evenNumber = []

    for i in range(1,21):
        if(i % 2 == 0):
            evenNumber.append(i)
    
    print("TID of Even thread : ", threading.get_ident())
    print("First 10 Even Numbers are : ", evenNumber)

def displayOddNumbers():

    oddNumber = []

    for i in range(1,21):
        if(i % 2 != 0):
            oddNumber.append(i)
    
    print("TID of Odd thread : ", threading.get_ident())
    print("First 10 Odd Numbers are : ", oddNumber)

def main():
    print("TID of Main thread : ", threading.get_ident())

    start_time = time.perf_counter()

    even_Thread = threading.Thread(target=displayEvenNumbers)
    odd_Thread = threading.Thread(target=displayOddNumbers)

    even_Thread.start()
    odd_Thread.start()

    even_Thread.join()
    odd_Thread.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")

if __name__=="__main__":
    main()