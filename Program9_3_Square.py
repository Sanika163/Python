# Write a program which accepts one number and prints square of that number
#Input: 5
#Output: 25

def Square(No):
    return No * No

def main():

    No = int(input("Enter Number :"))

    Ret = Square(No)
    print("Square of",No, "is :", Ret)

if(__name__ == "__main__"):
    main()