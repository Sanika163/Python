# Write a program which accepts one number and prints sum of digits
# Input : 123
# Output : 6

def SumOfDigits(No):
    Sum = 0

    while(No != 0):
        digit = No % 10
        No = No // 10
        Sum = Sum + digit

    return Sum

def main():
    No = int(input("Enter Number :"))

    Ret = SumOfDigits(No)

    print("Sum of Digits is :", Ret)
    
if(__name__ == "__main__"):
    main()