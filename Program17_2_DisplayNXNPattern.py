# 2. Write a program which accept one number and display below pattern. 5

# Input:  5

# Output:
#        *   *   *   *   *
#        *   *   *   *   *
#        *   *   *   *   *
#        *   *   *   *   *
#        *   *   *   *   *

def DisplayPattern(N):
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            print("*", end = ' ')
            j = j+1
        print()
        i = i+1


def main():
    N = int(input("Enter Number : "))

    DisplayPattern(N)

if __name__=="__main__":
    main()
