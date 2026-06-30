# Write a program which accepts one number and prints all even numbers till that number.
# Input : 10
# Output: 2 4 6 8 10

def EvenNumbers(No):
    Result = []

    for i in range(2,No+1):
        if(i%2 == 0):
            Result.append(i)

    return Result

def main():
    No = int(input("Enter Number :"))

    Ret = EvenNumbers(No)
    print("Even Numbers till:", Ret)

if(__name__ == "__main__"):
    main()