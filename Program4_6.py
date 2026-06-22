# Dictionary

def main():
    student = {
        "Name": "John",
        "Age": 22,
        "Country": "India"
    }

    print(student)
    print(student["Name"])
    print(student["Age"])
    print(student["Country"])

    student["Course"] = "Python"    #Adding new key-value pair

    student["Age"] = 28 #Updating a value

    print(student)

if (__name__ == "__main__"):
    main()