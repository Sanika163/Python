# 2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

# Input: Number of elements: 7

# Input Elements: 13  5   45  7   4   56 34

# Output: 56

def Maximum(Numbers):
    Max = 0

    for No in Numbers:
        if(No > Max):
            Max = No

    return Max
    
def AcceptNumbers(N):
    NumberList = []

    for i in range(N):
        No = int(input())
        NumberList.append(No)

    return NumberList

def main():
    N = int(input("Enter how many numbers you want to enter : "))

    Numbers = AcceptNumbers(N)
    print(f"Numbers enter by user : {Numbers}")

    Ret = Maximum(Numbers)
    print(f"Maximum from {N} Numbers is: {Ret}")

if __name__=='__main__':
    main()