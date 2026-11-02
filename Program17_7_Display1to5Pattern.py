# 7. Write a program which accept one number and display below pattern.

# Input:

# Output:

#   1   2   3   4   5
#   1   2   3   4   5
#   1   2   3   4   5
#   1   2   3   4   5 
#   1   2   3   4   5

def DisplayPattern(N):
    for i in range(N):
        for j in range(N):
            print(j+1, end=' ')

        print()
    
def main():
    N = int(input("Enter Number : "))

    DisplayPattern(N)

if __name__=="__main__":
    main()
