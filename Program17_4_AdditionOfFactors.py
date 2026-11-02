# 4. Write a program which accept one number form user and return addition of its factors.

# Input: 12

# Output: 16 (1+2+3+4+6)

def AdditionOfFactors(N):
    fact_Sum = 0
    for i in range(1, N):
        if(N % i == 0):
            fact_Sum = fact_Sum + i

    return fact_Sum


def main():
    N = int(input("Enter Number : "))

    Ret = AdditionOfFactors(N)
    print(f"Addition Of Factors of {N} is : {Ret}")

if __name__=="__main__":
    main()