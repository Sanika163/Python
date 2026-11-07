# 5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to CheckPrime() function which is part of our user defined module named as CheckNumberMod. 
# Name of the function from main python file should be ListPrime().

# Input: Number of elements: 11

# Input Elements: 13  5   45  7   4   56  10  34  2   5   8

# Output: 54 (13+5+7+2+5)

import CheckNumberMod as ChkNum

def AcceptNumbers(N):
    NumberList = []

    for i in range(N):
        No = int(input())
        NumberList.append(No)

    return NumberList

def ListPrime(Numbers):

    sum = 0

    for No in Numbers:
        bRet = ChkNum.CheckPrime(No)

        if(bRet == True):
            sum = sum + No

    return sum
def main():
    N = int(input("Enter how many numbers you want to enter : "))

    Numbers = AcceptNumbers(N)
    print(f"Numbers enter by user : {Numbers}")

    Ret = ListPrime(Numbers)
    print(f"Summation of Prime Numbers is: {Ret}")

if __name__=='__main__':
    main()