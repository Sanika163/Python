# Write a lambda function which accepts two numbers and returns maximum number

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

    print(f"Maximum Number is : {Maximum(No1, No2)}")

if (__name__ == "__main__"):
    main()