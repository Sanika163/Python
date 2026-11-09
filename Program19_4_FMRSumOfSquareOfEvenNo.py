# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even.
# Map function will calculate its square. 
# Reduce will return addition of all that numbers.

# Input List [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

# List after filter = [2, 4, 4, 2, 8, 10] List after map = [4, 16, 16, 4, 64, 100]

# Output of reduce = 204

from functools import reduce

def main():
    N = int(input("Enter number of elements you want to enter : "))
    
    Numbers = []

    for i in range(N):
        No = int(input())
        Numbers.append(No)

    print(f"Numbers Entered by User are : {Numbers}")

    fRet = list(filter(lambda X : X % 2 == 0, Numbers))
    print(f"Numbers after filter (Even Numbers): {list(fRet)}")

    mRet = list(map(lambda X : X * X, fRet))
    print(f"Numbers after Map : {list(mRet)}")

    reduceResult = reduce(lambda X, Y : X + Y, mRet)
    print(f"Final Result after Reduce : {reduceResult}")

if __name__ == '__main__':
    main()
