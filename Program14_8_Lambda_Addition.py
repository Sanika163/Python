# Write a lambda function which accepts two number and returns addition.

def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))

    Addition = lambda No1, No2 : No1 + No2

    print(f"Addition of {No1} & {No2} : {Addition(No1, No2)}")
    
if (__name__ == "__main__"):
    main()