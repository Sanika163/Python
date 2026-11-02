# 10. Write a program which accept number from user and return addition of digits in that number. 

# Input: 5187934

# Output: 37


def CountNoOfDigits(N):
    sumOfDigits = 0
    digit = 0 

    while (N != 0):
        digit = N % 10
        sumOfDigits = sumOfDigits + digit
        N = N // 10

    return sumOfDigits

    
def main():
    N = int(input("Enter Number : "))

    Ret = CountNoOfDigits(N)
    print(f"Sum of digits is : {Ret}")


if __name__=="__main__":
    main()