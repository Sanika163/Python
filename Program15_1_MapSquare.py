# Write a lambda function using map() which accepts a list of all numbers and returns a list of squares of each number.

def main():
    N = int(input("Enter Number of Elements : "))
    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} :")

        num = int(input())
        Data.append(num)

    Square = lambda No : (No ** 2)

    mData = list(map(Square, Data))

    print(f"Result of Map : {mData}")

if (__name__ == "__main__"):
    main()