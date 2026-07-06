# Write a lambda function which accepts one number and returns cube of that number

def main():
    No = int(input("Enter Number :"))

    Cube = lambda No : No ** 3

    print(f"Cube of {No} is {Cube(No)}")

if (__name__ == "__main__"):
    main()