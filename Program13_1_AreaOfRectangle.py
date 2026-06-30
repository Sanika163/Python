# Write a program which accepts length and breadth of rectangle and prints area.

def AreaOfRectangle(l, b):
    return l * b

def main():
    length = int(input("Enter length :"))
    breadth = int(input("Enter breadth :"))

    Ret = AreaOfRectangle(length, breadth)
    print("Area of Rectangle :", Ret)
    
if(__name__ == "__main__"):
    main()