# Write a program which accepts one number and prints the cube of that number

def Cube(No):
    return No * No * No

def main():

    No = int(input("Enter Number :"))

    Ret = Cube(No)
    print("Cube of",No, "is :", Ret)

if(__name__ == "__main__"):
    main()