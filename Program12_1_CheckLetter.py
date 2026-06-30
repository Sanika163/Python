# Write a program which accepts one character and checks whether it is vowel or consonant
# Input : a
# Output : Vowel

def CheckLetter(Value):
    if(Value == 'a' or Value == 'A' or Value == 'e' or Value == 'E' or Value == 'i' or Value == 'I' or Value == 'o' or Value == 'O' or Value == 'u' or Value == 'U'):
        return True
    else:
        return False

def main():
    char1 = input("Enter Character :")

    Ret = CheckLetter(char1)

    if(Ret == True):
        print("Vowel")
    else:
        print("Consonant")
    
if(__name__ == "__main__"):
    main()