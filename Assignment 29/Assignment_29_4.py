# Write a program which accepts two file names through command line arguments and compares the contents of both files.
#    If both files contain the same contents, display Success
#    Otherwise display Failure
# Input (Command Line):Demo.txt Hello.txt
# Expected Output:Success OR Failure

import sys

def main():
    try:
        
        if len(sys.argv) < 3:
            print("Some argumens are missing")
            sys.exit()

        
        fName1=sys.argv[1]
        fName2=sys.argv[2]
        
        
        fObj1=open(fName1,"r")
        fObj2=open(fName2,"r")

        Data1=fObj1.read()
        Data2=fObj2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")
        
        fObj1.close()
        fObj2.close()
        


    except FileNotFoundError as fobj:
        print("File not exist in current directory")

if __name__ == "__main__":
    main()