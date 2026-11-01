# 10. Write a program which accept name from user and display length of its name.

# Input: Programming
# Output: 11

def DisplayStrLength(str1):

    #return len(str1)

    count = 0
    
    for char in str1:
         count = count + 1
    
    return count

def main():
        str1 = str(input("Enter string : "))
        
        Ret = DisplayStrLength(str1)
        print(f"Length of string {str1} is : {Ret}")

if __name__=="__main__":
    main()
