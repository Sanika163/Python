'''1. Write a Python program to implement a class named Demo with the following specifications:
The class should contain two instance variables: nol and no2.
The class should contain one class variable named Value.
Define a constructor (init) that accepts two parameters and initializes the instance variables.
Implement two instance methods:
Fun()-displays the values of instance variables nol and no2.
Gun()-displays the values of instance variables nol and no2.
Create two objects of the Demo class as follows:
Obj1 Demo (11, 21)
Obj2 Demo (51, 101)
Call the instance methods in the given sequence:
Objl.Fun()
Obj2.Fun()
Objl.Gun()
Obj2.Gun()'''

class Demo:
    Value = 10

    def __init__(self, i, j):
        self.No1 = i
        self.No2 = j

    def Fun(self):
        print("Inside Fun Function...")
        print(f"Value of No1 from Fun: {self.No1}")
        print(f"Value of No2 from Fun: {self.No2}")

    def Gun(self):
        print("Inside Gun Function...")
        print(f"Value of No1 from Gun: {self.No1}")
        print(f"Value of No2 from Gun: {self.No2}")

def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

    print(f"Class Variable Value : {Demo.Value}")

if __name__=="__main__":
    main()