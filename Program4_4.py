#What happens when you modify string internally

def main():
    name = "Sanika"
    print(name)
    print(id(name))

    name = name + "Jadhav"

    print(name)
    print(id(name))

if (__name__ == "__main__"):
    main()