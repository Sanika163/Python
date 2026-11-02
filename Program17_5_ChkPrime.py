# 5. Write a program which accept one number for user and check whether number is prime or not.

# Input: 5

# Output: It is Prime Number

def CheckPrime(N):

    bflag = False

    for i in range(2, N):
        if(N % i == 0):
            print(i)
            bflag = True
            break

    return bflag

def main():
    N = int(input("Enter Number : "))

    bRet = CheckPrime(N)

    if(bRet == True):
        print(f"{N} is Not a Prime Number")
    else:
        print(f"{N} is a Prime Number")


if __name__=="__main__":
    main()
