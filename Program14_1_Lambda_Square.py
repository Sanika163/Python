# Write a lambda function which accepts one number and returns sqaure of that number.

def main():
    No = int(input("Enter Number :"))

    Square = lambda No : No ** 2

    print(f"Square of {No} is {Square(No)}")

if (__name__ == "__main__"):
    main()