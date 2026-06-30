# Write a program which accepts one number and prints multiplication table of that number.
#Input : 4
#Output : 4 8 12 16 20 24 28 32 36 40

def MultilicationTable(No):
    Result = []
    for i in range(1,11):
        Mult = i * No
        Result.append(Mult)

    return Result

def main():

    No = int(input("Enter Number :"))

    print("Table of", No, "is :")

    Ret = MultilicationTable(No)

    for i in range(len(Ret)):
        print(Ret[i])


if(__name__ == "__main__"):
    main()