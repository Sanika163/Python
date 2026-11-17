# 2: Design a Python application that creates two threads.

# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.
 
import time
import threading

def Maximum(Numbers):
    Max = Numbers[0]
    for No in Numbers:
        if(No > Max):
            Max = No
        
    print(f"Maximum number from list is : {Max}")

def Minimum(Numbers):
    Min = Numbers[0]
    for No in Numbers:
        if(No < Min):
            Min = No
        
    print(f"Minimum number from list is : {Min}")

def main():

    N = int(input("Enter how many numbers you want :"))

    Numbers = []

    for i in range(N):
        Num = int(input())
        Numbers.append(Num)

    start_time = time.perf_counter()

    Maximum_Thread = threading.Thread(target=Maximum, args=(Numbers, ))
    Minimum_Thread = threading.Thread(target=Minimum, args=(Numbers, ))
    
    Maximum_Thread.start()
    Minimum_Thread.start()

    Maximum_Thread.join()
    Minimum_Thread.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")
    
if __name__=="__main__":
    main()