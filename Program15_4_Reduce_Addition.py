# Write a lambda function using reduce() which accepts a list of all numbers and returns the addition of all elements.
from functools import reduce

def main():

    N = int(input("Enter Number of Elements :"))

    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} : ")
        
        Num = int(input())
        Data.append(Num)

    Addition = reduce(lambda No1, No2 : No1 + No2, Data)

    print("Addition of all Numbers :", Addition)

if __name__ == "__main__":
    main()