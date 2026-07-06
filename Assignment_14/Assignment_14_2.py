# Write a lmbda function which accepts one number and returns cube of that number

cubeLmbda = lambda a : a*a*a

def main():   
    no1 = int(input("Enter number:"))
    print("cube of number is: ",cubeLmbda(no1))
if __name__ == "__main__":
    main()    