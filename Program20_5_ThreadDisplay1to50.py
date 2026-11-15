# 5: Design a Python application that creates two threads named Thread1 and Thread2.

# Thread1 should display numbers from 1 to 50.

# Thread2 should display numbers from 50 to 1 in reverse order.

# Ensure that: Thread2 starts execution only after Thread1 has completed.

import time
import threading

def display1to50():
    print("Thread 1 Started the execution ...")

    for i in range(1, 51, 1):
        print(i)

def display50to1():
    print("Thread 2 Started the execution ...")

    for i in range(50, 0, -1):
        print(i)

def main():

    start_time = time.perf_counter()

    display1to50_Thread = threading.Thread(target=display1to50)
    display50to1_Thread = threading.Thread(target=display50to1)
    
    display1to50_Thread.start()
    display1to50_Thread.join()
    
    display50to1_Thread.start()
    display50to1_Thread.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")
    
if __name__=="__main__":
    main()