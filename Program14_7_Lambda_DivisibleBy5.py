# Write a lambda function which accepts one number and returns True if divisible by 5.

def main():
    No = int(input("Enter Number : "))

    CheckDivisibleByFive = lambda No : (No % 5 == 0)

    print(f"Is {No} divisible by 5 : {CheckDivisibleByFive(No)}")
    
if (__name__ == "__main__"):
    main()