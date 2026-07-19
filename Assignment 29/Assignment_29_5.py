# Write a program which accepts a file name and one string from the user and 
# returns the frequency (count of occurrences) of that string in the file.
# Input : Demo.txt Marvellous
# Expected Output:Count how many times "Marvellous" appears in Demo.txt.

import sys

def main():
    try:      
        fName=input("Enter file name: ")
        word = input("Enter word: ")

        fObj=open(fName,"r")

        count =0 

        for line in fObj:
            count += line.count(word)

        fObj.close()       
        print(f"{word} appears in {fName} : {count}")

    except FileNotFoundError as fobj:
        print("File not exist in current directory")

if __name__ == "__main__":
    main()