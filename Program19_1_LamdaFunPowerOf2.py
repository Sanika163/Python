# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.

# Input: 4

# Output: 16

# Input: 6

# Output: 64

def main():
    N = int(input("Enter Number : "))

    Ret = lambda N : 2**N
    print(f"2 raised to {N} is : {Ret(N)}")

if __name__ == '__main__':
    main()