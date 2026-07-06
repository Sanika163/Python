# Write a lambda function which accepts three numbers and returns largest number.

# def LargestNumber(No1, No2, No3):
#     if(No1>No2 and No1>No3):
#         return No1
#     elif(No2>No1 and No2>No3):
#         return No2
#     else:
#         return No3
    
def main():
    No1 = int(input("Enter First Number : "))
    No2 = int(input("Enter Second Number : "))
    No3 = int(input("Enter Third Number : "))

#    LargestNumber = lambda No1, No2, No3 : max(No1, No2, No3)

    LargestNumber = lambda No1, No2, No3 : No1 if No1 > No2 and No1 > No3 else (No2 if No2 > No3 else No3)

    print(f"Largest Number is : {LargestNumber(No1, No2, No3)}")
    
if (__name__ == "__main__"):
    main() 