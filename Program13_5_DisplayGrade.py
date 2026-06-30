# Write a program which accpets marks and displays grade
#Condition Example:
#  >= 75 -> Distinction
#  >= 60 -> First Class
#  >= 50 -> Second Class
#  < 50 -> Fail 

def DisplayGrade(Marks):
    if(Marks >= 75):
        print("Distinction")
    elif(Marks >= 60 and Marks < 75):
        print("First Class")
    elif(Marks >= 50 and Marks < 60):
        print("Second Class")
    else:
        print("Fail")
    

def main():
    No = int(input("Enter Marks :"))

    Ret = DisplayGrade(No)
    
if(__name__ == "__main__"):
    main()