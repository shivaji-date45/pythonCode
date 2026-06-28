# Write a program which accepts one character 
# and checks whether it is vowel or not

def CheckCharIsVowel(char):
    if  char.lower() in 'aeiou':
        return True
    else:
        return False
    

def main():
    char=input("Enter character: ")
    
    if CheckCharIsVowel(char) == True:
        print("Vowel")
    else:
        print("Not Vowel")

if __name__ == "__main__":
    main()    