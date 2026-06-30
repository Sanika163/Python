# Write a program which accepts one number and prints the sum of first N Natural numbers
# Input: 5
# Output: 15

def SumOfNumbers(No):
    Sum = 0
    for i in range(No+1):
        Sum = Sum + i

    return Sum

def main():
    No = int(input("Enter Number :"))

    Ret = SumOfNumbers(No)
    print("Summation of Numbers :", Ret)

if(__name__ == "__main__"):
    main()