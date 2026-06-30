# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division

def MathOperations(No1, No2):
    print("Addition :", No1+No2)
    print("Subtraction :", No1-No2)
    print("Multiplication :", No1*No2)
    print("Division :", No1/No2)

def main():
    Value1 = int(input("Enter 1st Number :"))
    Value2 = int(input("Enter 2nd Number :"))

    Ret = MathOperations(Value1, Value2)
    
if(__name__ == "__main__"):
    main()