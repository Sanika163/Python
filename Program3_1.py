#Accept two numbers and return their multiplication

def Multiplication(No1, No2):
    mult = No1 *No2
    return mult

def main():
    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())
        
    
    result = Multiplication(No1, No2)
    print("Result is: ", result)

if __name__ == "__main__":
    main()