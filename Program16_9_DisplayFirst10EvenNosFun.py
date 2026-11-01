# 9. Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def DisplayFirst10EvenNo():

    for i in range(2,21,2):
        if(i%2 == 0):
            print(i, end = ' ')

def main():

    DisplayFirst10EvenNo()

if __name__=="__main__":
    main()