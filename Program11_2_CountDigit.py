# Write a program which accepts one number and prints count of digit in that number
# Input : 7521
# Output : 4

def CountDigit(No):
    Count = 0

    while(No != 0):
        No = No // 10
        Count = Count + 1

    return Count

def main():
    No = int(input("Enter Number :"))

    Ret = CountDigit(No)

    print("Count of Digits is :", Ret)
    
if(__name__ == "__main__"):
    main() 