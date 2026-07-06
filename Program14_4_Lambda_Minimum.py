# Write a lambda function which accepts two numbers and returns minimum number

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

    print(f"Minimum Number is : {Minimum(No1, No2)}")

if (__name__ == "__main__"):
    main()