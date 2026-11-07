# 4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

# Input: Number of elements: 11

# Input Elements: 13   5   45   7   4   56  5   34  2   5   65

# Element to search: 5

# Output: 3

def SearchFrequencyOfNo(Numbers, Search):
    freq = 0

    for No in Numbers:
        if(No == Search):
            freq = freq + 1

    return freq
    
def AcceptNumbers(N):
    NumberList = []

    for i in range(N):
        No = int(input())
        NumberList.append(No)

    return NumberList

def main():
    N = int(input("Enter how many numbers you want to enter : "))

    Numbers = AcceptNumbers(N)
    print(f"Numbers enter by user : {Numbers}")

    Value = int(input("Enter Number whose frequency you want to search : "))
    
    Ret = SearchFrequencyOfNo(Numbers, Value)
    print(f"Frequency of {Value} is: {Ret}")

if __name__=='__main__':
    main()