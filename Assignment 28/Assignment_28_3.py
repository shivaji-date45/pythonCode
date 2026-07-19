#Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
#Input:Demo.txt
#Expected Output:Display each line of Demo.txt one by one.

def main():
    try:
        fName=input("Enter file name: ")
        fObj=open(fName,"r")
        
        wordCount = 0
        for line in fObj:
           print(line,end="")
        
        fObj.close()
        
    except FileNotFoundError as fobj:
        print("File not exist in current directory")
if __name__ == "__main__":
    main()