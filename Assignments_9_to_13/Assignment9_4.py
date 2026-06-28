# Write a program which accepts one number
# and prints cube of that number

def CubeOfNumber(No):
    return No*No*No

def main():
    No=int(input("Enter Number:"))
    print("square of number is:",CubeOfNumber(No))

if __name__ == "__main__":
    main()    