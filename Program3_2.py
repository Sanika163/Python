#Function with parameter and without parameter

def CheckEvenOdd(Value1):   #Function with parameter
    if(Value1 % 2 == 0):
        print(Value1, "is Even Number")
    else:
        print(Value1, "is Odd Number")

def Display():  #Function without parameter
    print("This is exmple of Function with no Parameter")

def main():
    print("Enter Number:")
    No1 = int(input())

    CheckEvenOdd(No1)

    Display()

if(__name__ == "__main__"):
    main()