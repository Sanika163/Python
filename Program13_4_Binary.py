# Write a program which accepts one number and prints binary equivalent

def Binary(No):

    binary =""

    while No > 0:
        remainder = No % 2
        binary = str(remainder) + binary
        No = No // 2
    
    return binary

def main():
    No = int(input("Enter Number :"))

    Ret = Binary(No)
    
    print("Binary :", Ret)
    
if(__name__ == "__main__"):
    main()
