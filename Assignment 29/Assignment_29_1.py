# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
#Input:Demo.txt
#Expected Output:Display whether Demo.txt exists or not.

import os

def main():
    try:
        fName=input("Enter file name: ")
        
        ret=os.path.exists(fName)

        if ret == True:
            print(f"{fName} exists")
        else:
            print(f"{fName} not exists")


    except FileNotFoundError as fobj:
        print("File not exist in current directory")
if __name__ == "__main__":
    main()