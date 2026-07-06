# Write a program which accept number from user and print that number of "*" on Screen
# e.g Input : 5             Output : * * * * * *


def PrintStar(num):   
    print(f"Input : {num}                Output :",end=" ")
    for i in range(num):
        print("*",end=" ")

def main():
    num=int(input("Enter number: "))  
    PrintStar(num)

if __name__ == "__main__":
    main()    