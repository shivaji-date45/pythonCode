# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt,
# and copies all contents from the given file into Demo.txt.
# Input (Command Line):ABC.txt
# Expected Output:Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys

def main():
    try:

        fName=sys.argv[1]

        fObj=open(fName,"r")
        newFileObj=open("Demo.txt","w")

        for line in fObj:
            newFileObj.write(line)
        
        fObj.close()
        newFileObj.close()

        print(f"Content of file {fName} copied to  Demo.txt")

    except FileNotFoundError as fobj:
        print("File not exist in current directory")

if __name__ == "__main__":
    main()