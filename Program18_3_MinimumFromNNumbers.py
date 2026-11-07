# 3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

# Input: Number of elements: 4

# Input Elements: 13  5   45  7

# Output: 5

def Minimum(Numbers):
    Min = Numbers[0]

    for No in Numbers:
        if(No < Min):
            Min = No

    return Min
    
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

    Ret = Minimum(Numbers)
    print(f"Minimum from {N} Numbers is: {Ret}")

if __name__=='__main__':
    main()