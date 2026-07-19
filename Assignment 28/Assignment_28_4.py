#Write a program which accepts two file names from the user.
#   First file is an existing file
#   Second file is a new file
#Copy all contents from the first file into the second file.
#Input:ABC.txt Demo.txt
#Expected Output:Contents of ABC.txt copied into Demo.txt.

def main():
    try:
        fName=input("Enter existing file name: ")
        newFileName= input("Enter new file name: ")

        fObj=open(fName,"r")
        newFileObj = open(newFileName,"w")
        
        for line in fObj:
            newFileObj.write(line)
        
        fObj.close()
        newFileObj.close()
        
        print(f"Contents of {fName} copied into {newFileName}.")

    except FileNotFoundError as fobj:
        print("File not exist in current directory")
if __name__ == "__main__":
    main()