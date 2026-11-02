# 6. Write a program which accept one number and display below pattern.

# Input: 5

# Output:
#            *  *   *   *   *
#            *  *   *   *
#            *  *   *
#            *  *
#            *

def DisplayPattern(N):

    for i in range(0, N):   
        for j in range(0, N-i):
            print("*", end = ' ')
            
        print()
    
def main():
    N = int(input("Enter Number : "))

    bRet = DisplayPattern(N)

if __name__=="__main__":
    main()