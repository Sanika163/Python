#None
#Is the None is same as 0, False, empty string

def main():
    name = None

    print(name) #None
    print(type(name))   #NoneType

    print(None == 0)  #False
    print(None == False)  #False
    print(None == '') #False

if (__name__ == "__main__"):
    main()