# 3: Design a Python application that creates two threads named EvenList and OddList.

# Both threads should accept a list of integers as input.

# The EvenList thread should:
#    - Extract all even elements from the list.
#    - Calculate and display their sum.

# The OddList thread should:
#    - Extract all odd elements from the list.
#    - Calculate and display their sum.

# Threads should run concurrently.

import time
import threading

def displayEven(Numbers):

    even = []
    sumEven = 0

    for num in Numbers:
        if(num % 2 == 0):
            even.append(num)
            sumEven = sumEven + num
            
    print(f"Even Numbers are : {even}")
    print(f"Sum of Even Numbers is : {sumEven}")

def displayOdd(Numbers):

    odd = []
    sumOdd = 0

    for num in Numbers:
        if(num % 2 != 0):
            odd.append(num)
            sumOdd = sumOdd + num
            
    print(f"Odd Numbers are : {odd}")
    print(f"Sum of Odd Numbers is : {sumOdd}")

def main():

    N = int(input("Enter Number of elements you want: "))
    Numbers = []
    for i in range(N):
        No = int(input())
        Numbers.append(No)

    print("Elements entered by user : ", Numbers)

    start_time = time.perf_counter()

    evenFactor_Thread = threading.Thread(target=displayEven, args = (Numbers,))
    oddFactor_Thread = threading.Thread(target=displayOdd, args = (Numbers,))

    evenFactor_Thread.start()
    oddFactor_Thread.start()

    evenFactor_Thread.join()
    oddFactor_Thread.join()

    end_time = time.perf_counter()

    print("Exit from Main")
    print(f"Time required is : {end_time - start_time:.4f}")

if __name__=="__main__":
    main()