#Predict O/P

def main():
    s = "Python"
    print(s)
    print(id(s))

    s[0] = "J"  #TypeError: 'str' object does not support item assignment

    print(s)
    print(id(s))

if (__name__ == "__main__"):
    main()