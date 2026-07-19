#Write a program which accepts a file name from the user and counts the total number of words in that file.
#Input:Demo.txt
#Expected Output:Total number of words in Demo.txt.

def main():
    try:
        fName=input("Enter file name: ")
        fObj=open(fName,"r")
        
        wordCount = 0
        for line in fObj:
            words = line.split()
            wordCount += len(words)

        fObj.close()
        print(f"Total numbers of words in file is : {wordCount}")
        
    except FileNotFoundError as fobj:
        print("File not exist in current directory")
if __name__ == "__main__":
    main()