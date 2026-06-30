# Write a program which contains one function ChkGreater() that accepts two numbers and prints the grater number
#Input: 10, 20
#Output: 20 is Greater

def ChkGreater(Value1, Value2):
    if(Value1 > Value2):
        return Value1
    else:
        return Value2

def main():

    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter First Number :"))

    Ret = ChkGreater(No1, No2)
    print(Ret, "is Greater")

if(__name__ == "__main__"):
    main()