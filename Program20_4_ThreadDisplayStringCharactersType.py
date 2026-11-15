# 4: Design a Python application that creates three threads named Small, Capital, and Digits.

# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.

# Each thread must also display:
#    - Thread ID
#    - Thread Name


import time
import threading

def countCapital(Str):

    capital = 0

    for char in Str:
        if char >= 'A' and char <= 'Z':
            capital = capital + 1

    print(f"Current Thread Name is : {threading.current_thread().name}")
    print(f"Thread ID of {threading.current_thread().name} Thread is : {threading.get_ident()}")
    print(f"Count of Capital characters from {Str} are : {capital}")

def countSmall(Str):
    small = 0

    for char in Str:
        if char >= 'a' and char <= 'z':
            small = small + 1

    print(f"Current Thread Name is : {threading.current_thread().name}")
    print(f"Thread ID of {threading.current_thread().name} Thread is : {threading.get_ident()}")
    print(f"Count of Small characters from {Str} are : {small}")

def countDigit(Str):
    digit = 0

    for char in Str:
        if char >= '0' and char <= '9':
            digit = digit + 1

    print(f"Current Thread Name is : {threading.current_thread().name}")
    print(f"Thread ID of {threading.current_thread().name} Thread is : {threading.get_ident()}")
    print(f"Count of Digits characters from {Str} are : {digit}")

def main():

    print("Enter Strings for Thread : ")

    str = []

    for i in range(3):
        str.append(input(f"Enter String {i+1} for T{i+1} : "))
    
    start_time = time.perf_counter()

    countCapital_Thread = threading.Thread(target=countCapital, args = (str[0],), name='Capital')
    countSmall_Thread = threading.Thread(target=countSmall, args = (str[1],), name= 'Small')
    countDigit_Thread = threading.Thread(target=countDigit, args = (str[2],), name= 'Digit')
    
    countCapital_Thread.start()
    countSmall_Thread.start()
    countDigit_Thread.start()

    countCapital_Thread.join()
    countSmall_Thread.join()
    countDigit_Thread.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.4f}")
    print("Exit from Main")

if __name__=="__main__":
    main()