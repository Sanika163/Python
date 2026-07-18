# Write a lambda function using filter() which accepts a list of strings and returns list of strings having length greater than 5.

def main():

    N = int(input("Enter Number of Strings :"))

    Data = []

    for i in range(N):
        print(f"Enter String {i+1} : ")
        
        str = input()
        Data.append(str)

    strLenGreaterThanFive = list(filter(lambda str : len(str) > 5, Data))

    print("Strings having length greater than 5 :", strLenGreaterThanFive)

if __name__ == "__main__":
    main()