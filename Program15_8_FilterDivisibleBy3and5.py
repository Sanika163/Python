# Write a lambda function using filter() which accepts a list of numbers and returns the list of numbers divisible by 3 and 5.

def main():

    N = int(input("Enter Number of Elements :"))

    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} : ")
        
        num = int(input())
        Data.append(num)

    DivisibleBy3and5 = list(filter(lambda No : No % 3 == 0 and No % 5 == 0, Data))

    print("Numbers Divisible by 3 and 5 :", DivisibleBy3and5)

if __name__ == "__main__":
    main()