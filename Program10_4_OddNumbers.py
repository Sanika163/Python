# Write a program which accepts one number and prints all Odd numbers till that number.
# Input : 10
# Output: 1 3 5 7 9

def OddNumbers(No):
    Result = []

    for i in range(2,No+1):
        if(i%2 != 0):
            Result.append(i)

    return Result

def main():
    No = int(input("Enter Number :"))

    Ret = OddNumbers(No)
    print("Odd Numbers till:", Ret)

if(__name__ == "__main__"):
    main()