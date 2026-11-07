# 1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

# Input Elements: 13

# Input: Number of elements: 6

# Output: 130

def AcceptNumbers(N):

    print(f"Enter {N} Numbers : ")

    NumberList = []

    for i in range(N):
        No = int(input())
        NumberList.append(No)

    return NumberList

def Summation(Numbers):

    sum = 0

    for No in Numbers:
        sum = sum + No

    return sum

def main():
    N = int(input("Enter how many numbers you want to enter : "))

    Numbers = AcceptNumbers(N)
    print(f"Numbers enter by user : {Numbers}")

    Ret = Summation(Numbers)
    print(f"Summation of {N} Numbers : {Ret}")

if __name__ == '__main__':
    main()