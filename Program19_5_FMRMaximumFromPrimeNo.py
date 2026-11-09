# 5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]

# List after filter = [2, 11, 17, 23, 31]

# List after map = [4, 22, 34, 46, 62]

# Output of reduce = 62

import math
from functools import reduce

def CheckPrime(No):

    if(No <= 1):
        return False
    
    for i in range(2, int(No**0.5) + 1):
        if(No % i == 0):
            return False
        
    return True

def main():
    N = int(input("Enter number of elements you want to enter : "))
    
    Numbers = []

    for i in range(N):
        No = int(input())
        Numbers.append(No)

    print(f"Numbers Entered by User are : {Numbers}")

    fRet = list(filter(lambda X : CheckPrime(X), Numbers))
    print(f"Numbers after filter (Prime Numbers): {list(fRet)}")

    mRet = list(map( lambda X : X *2, fRet))
    print(f"Numbers after Map : {list(mRet)}")

    reduceResult = reduce(lambda X, Y : X if X > Y else Y, mRet)
    print(f"Final Result after Reduce : {reduceResult}")

if __name__ == '__main__':
    main()
