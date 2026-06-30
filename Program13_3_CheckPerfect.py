# Write a program which accepts one number and checks whether it is perfect number or not
# Input : 6
# Output : Perfect Number

def CheckPerfect(No):
    Sum = 0
    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i

    if(No == Sum):
        return True
    else:
        return False

def main():
    No = int(input("Enter Number :"))

    Ret = CheckPerfect(No)
    
    if(Ret == True):
        print("Perfect Number")
    else:
        print("Not a Perferct Number")
    
if(__name__ == "__main__"):
    main()