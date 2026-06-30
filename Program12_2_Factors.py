# Write a program which accepts one number and prints its factors.
# Input : 12
# Output : 1 2 3 4 6 12

def Factors(No):
    flist = []

    for i in range(1, No+1):
        if(No%i == 0):
            flist.append(i)

    return flist

def main():
    char1 = int(input("Enter Character :"))

    Ret = Factors(char1)

    print("Factors :",Ret)
    
if(__name__ == "__main__"):
    main()