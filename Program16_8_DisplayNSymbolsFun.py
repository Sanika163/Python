
# 8. Write a program which accept number from user and print that number of "*" on screen.

# Input: 5
# Output: * * * * *

def DisplaySymbolNtimes(N):

    for i in range(N):
        print("*\t", end = ' ')

def main():

    N = int(input("Enter No : "))

    DisplaySymbolNtimes(N)

if __name__=="__main__":
    main()

