# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements

from functools import reduce

def main():

    N = int(input("Enter Number of Elements :"))

    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} : ")
        
        Num = int(input())
        Data.append(Num)

    Product = reduce(lambda No1, No2 : No1 * No2, Data)

    print("Product of all Elements is :", Product)

if __name__ == "__main__":
    main()