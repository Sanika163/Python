# 2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.

# Input: 4  3

# Output: 12

def main():
    No1 = int(input("Enter 1st Number : "))
    No2 = int(input("Enter 2nd Number : "))

    Multiplication = lambda No1, No2 : No1 * No2
    print(f"Product of {No1} & {No2} is : {Multiplication(No1, No2)}")

if __name__ == '__main__':
    main()
