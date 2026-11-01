# 5. Write a program which display 10 to 1 on screen.
#  Take N input from user. 
# Output: 10 (N)
# 10   9   8   7   6   5   4   3   2   1

def DisplayReverseNo(N):
    for i in range(N, 0, -1):
        print(i, end=' ')

def main():

    N = int(input("Enter No : "))

    DisplayReverseNo(N)

if __name__=="__main__":
    main()