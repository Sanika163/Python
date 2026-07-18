# Write a lambda function using reduce() which accepts a list of all numbers and returns the maximum element.

from functools import reduce

def main():

    N = int(input("Enter Number of Elements :"))

    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} : ")
        
        Num = int(input())
        Data.append(Num)

    Maximum = reduce(lambda No1, No2 : No1 if No1 > No2 else No2, Data)

    print("Maximum Number is :", Maximum)

if __name__ == "__main__":
    main()