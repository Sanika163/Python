# 3. Write a program which accept one number from user and return its factorial.

# Input: 5

# Output: 120

def Factorial(N):
    fact = 1
    for i in range(1, N+1):
        fact = fact * i

    return fact


def main():
    N = int(input("Enter Number : "))

    Ret = Factorial(N)
    print(f"Factorial of {N} is : {Ret}")

if __name__=="__main__":
    main()