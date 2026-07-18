# Write a lambda function using filter() which accepts a list of all numbers and returns a list of even numbers.

def main():

    N = int(input("Enter Number of Elements :"))

    Data = []

    for i in range(N):
        print(f"Enter Element {i+1} : ")
        
        Num = int(input())
        Data.append(Num)

    EvenNums = list(filter(lambda x : x % 2 == 0, Data))

    print("List of Even Numbers :", EvenNums)

if __name__ == "__main__":
    main()