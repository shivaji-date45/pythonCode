#Write a program which accepts a file name from the user and counts how many lines are present in the file.
#Input:Demo.txt
#Expected Output:Total number of lines in Demo.txt.

def main():
    try:
        fName=input("Enter file name: ")
        fObj=open(fName,"r")
        
        lineCount = 0
        for line in fObj:
            lineCount += 1

        fObj.close()
        print(f"Total numbers of lines in {fName} : {lineCount}")

    except FileNotFoundError as fobj:
        print("File not exist in current directory")
if __name__ == "__main__":
    main()