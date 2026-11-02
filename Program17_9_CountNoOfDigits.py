# 9. Write a program which accept number from user and return number of digits in that number.

# Input: 5187934

# Output: 7

def CountNoOfDigits(N):
    digitCount = 0

    while (N != 0):
        N = N // 10
        digitCount = digitCount + 1

    return digitCount

    
def main():
    N = int(input("Enter Number : "))

    Ret = CountNoOfDigits(N)
    print(f"Number of digits are : {Ret}")


if __name__=="__main__":
    main()