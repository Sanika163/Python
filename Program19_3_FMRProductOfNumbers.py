# 3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.

# Input List [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# List after filter [76, 89, 86, 90, 70]

# List after map = [86, 99, 96, 100, 80]

# Output of reduce = 6538752000

from functools import reduce

def main():
    N = int(input("Enter number of elements you want to enter : "))
    
    Numbers = []

    for i in range(N):
        No = int(input())
        Numbers.append(No)

    print(f"Numbers Entered by User are : {Numbers}")

    fRet = list(filter(lambda X : X >= 70 and X <= 90, Numbers))
    print(f"Numbers after filter (Number>= 70 and Numbers <= 90): {list(fRet)}")

    mRet = list(map(lambda X : X+10, fRet))
    print(f"Numbers after Map : {list(mRet)}")

    reduceResult = reduce(lambda X, Y : X * Y, mRet)
    print(f"Final Result after Reduce : {reduceResult}")

if __name__ == '__main__':
    main()
