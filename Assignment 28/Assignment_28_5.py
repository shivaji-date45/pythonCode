#Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
#Input:Demo. txt Marvellous
#Expected Output: Display whether the word Marvellous is found in Demo.txt or not.

def main():
    try:
        fName=input("Enter existing file name: ")
        wordToSearch=input("Enter word to search in file: ")

        fObj=open(fName,"r")
        found = False

        for line in fObj:
            if wordToSearch in line:
                found=True

        fObj.close()
        if found == True:
            print(f"The word {wordToSearch} is found in {fName}.")
        else:
            print(f"The word {wordToSearch} is not found in {fName}.")


    except FileNotFoundError as fobj:
        print("File not exist in current directory")
if __name__ == "__main__":
    main()