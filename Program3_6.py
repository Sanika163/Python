#Program to display
#Data Type
#Memory Address
#Size in bytes entered by user

import sys

def main():
    Value = input("Enter any Value:")

    print(type(Value))
    print(id(type))
    print(sys.getsizeof(Value))

if (__name__ == "__main__"):
    main()