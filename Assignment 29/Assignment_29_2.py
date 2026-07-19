# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input:Demo.txt
# Expected Output:Display contents of Demo.txt on console.

def main():
    try:
        fName=input("Enter file name: ")
        
        fObj=open(fName,"r")

        Data=fObj.read()
        print(Data)

    except FileNotFoundError as fobj:
        print("File not exist in current directory")

if __name__ == "__main__":
    main()