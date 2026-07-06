# Write a lambda function which accepts one number and returns True if number is even otherwise False

def main():
    No = int(input(("Enter Number : ")))

    CheckEven = lambda No : (No % 2 == 0)

    print(f"{No} is Even Number : {CheckEven(No)}")
    
if (__name__ == "__main__"):
    main()