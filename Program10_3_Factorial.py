# Write a program which accepts one number and prints factorial of that numbers.
# Input: 5
# Output: 120

def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = i * fact
        
    return fact

def main():
    No = int(input("Enter Number :"))

    Ret = Factorial(No)
    print("Factorial is:", Ret)

if(__name__ == "__main__"):
    main()