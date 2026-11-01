# 3. Write a program which contains one function named as Addition() which accepts two numbers from user and return addition of that two numbers.

# Input: 11 5
# Output: 16

def Addition(No1, No2):
    return No1 + No2

def main():
    No1 = int(input("Enter 1st Number : "))

    No2 = int(input("Enter 2nd Number : "))

    Ret = Addition(No1, No2)

    print(f"Additin of {No1} & {No2} : ", Ret)

if __name__=="__main__":
    main()
