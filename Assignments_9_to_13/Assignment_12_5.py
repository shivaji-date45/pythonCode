# Write a program which accepts one number 
# and prints that many numbers starting in reverse



def main():
    No=int(input("Enter number: "))
    
    for i in range(No,0,-1):
        print(i)

if __name__ == "__main__":
    main()    