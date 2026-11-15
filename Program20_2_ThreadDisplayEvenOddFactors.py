# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter.

# The EvenFactor thread should:
#    - Identify all even factors of the given number.
#    - Calculate and display the sum of even factors.

# The OddFactor thread should:
#    - Identify all odd factors of the given number.
#    - Calculate and display the sum of odd factors.

# After both threads complete execution, the main thread should display the message: "Exit from main"

import time
import threading

def displayEvenFactor(No):

    evenFactor = []
    sumEven = 0

    for i in range(2, No+1):
        if(No % i == 0 and i % 2 == 0):
            evenFactor.append(i)
            sumEven = sumEven + i
            
    print(f"Even Factors of {No} are : {evenFactor}")
    print(f"Sum of Even Factors of {No} is : {sumEven}")

def displayOddFactor(No):

    oddFactor = []
    sumOdd = 0

    for i in range(1, No+1):
        if(No % i == 0 and i % 2 != 0):
            oddFactor.append(i)
            sumOdd = sumOdd + i
            
    print(f"Odd Factors of {No} are : {oddFactor}")
    print(f"Sum of Odd Factors of {No} is : {sumOdd}")

def main():

    No = int(input("Enter Number : "))

    start_time = time.perf_counter()

    evenFactor_Thread = threading.Thread(target=displayEvenFactor, args = (No,))
    oddFactor_Thread = threading.Thread(target=displayOddFactor, args = (No,))

    evenFactor_Thread.start()
    oddFactor_Thread.start()

    evenFactor_Thread.join()
    oddFactor_Thread.join()

    end_time = time.perf_counter()

    print("Exit from Main")
    print(f"Time required is : {end_time - start_time:.4f}")

if __name__=="__main__":
    main()