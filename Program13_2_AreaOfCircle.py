# Write a program which accepts radius of circle and prints area of circle

def AreaOfCircle(radius):
    PI = 3.14

    return PI * radius * radius

def main():
    radius = int(input("Enter radius :"))

    Ret = AreaOfCircle(radius)
    print("Area of Circle :", Ret)
    
if(__name__ == "__main__"):
    main()