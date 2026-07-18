# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers

def main():

    N = int(input("Enter Number of Elements :"))

    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} : ")
        
        num = int(input())
        Data.append(num)

    CountOfEvenNums = list(filter(lambda No : No % 2 == 0, Data))
    # CountOfEvenNums = len(list(filter(lambda No : No % 2 == 0, Data)))

    print("Count of Even Numbers is :", len(CountOfEvenNums))

if __name__ == "__main__":
    main()