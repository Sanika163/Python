# Write a lambda function using reduce() which accepts a list of all numbers and returns the minimum element.from functools import reduce

from functools import reduce

def main():

    N = int(input("Enter Number of Elements :"))

    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} : ")
        
        Num = int(input())
        Data.append(Num)

    Minimum = reduce(lambda No1, No2 : No1 if No1 < No2 else No2, Data)

    print("Minimum Number is :", Minimum)

if __name__ == "__main__":
    main()