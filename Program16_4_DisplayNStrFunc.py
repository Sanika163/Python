#4. Write a program which display 5 times Hello on screen.

# Output:

# Hello
# Hello
# Hello
# Hello
# Hello

def DisplayHello5times(N, str):

    for i in range(N):
        print(str)

def main():

    N = int(input("Enter No : "))
    str = "Hello"

    DisplayHello5times(N, str)

if __name__=="__main__":
    main()
