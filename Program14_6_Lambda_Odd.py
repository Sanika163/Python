# Write a lambda function which accepts one number and returns True if number is Odd otherwise False

def main():
    No = int(input(("Enter Number : ")))

    CheckOdd = lambda No : (No % 2 != 0)

    print(f"{No} is Odd Number : {CheckOdd(No)}")
    
if (__name__ == "__main__"):
    main()