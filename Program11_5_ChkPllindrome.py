# Write a program which accepts one number and checks whether it is pallindrome or not
# Input : 121
# Output : Pallindrome

def ReverseNo(No):
    Rev = 0
    digit = 0
    temp = No

    while(No != 0):
        digit = No % 10
        Rev = Rev * 10 + digit
        No = No // 10

    if(temp == Rev):
        return True
    else:
        return False

def main():
    No = int(input("Enter Number :"))

    Ret = ReverseNo(No)

    if(Ret == True):
        print("Pallindrome")
    else:
        print("Not a Pallindrome")
    
if(__name__ == "__main__"):
    main()