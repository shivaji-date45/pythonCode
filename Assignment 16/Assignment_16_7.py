# Write a program which accept number from user and returns True if number is divisible by 5
# otherwise return false


def isDivisibleByFive(num):   
   return True if num%5 == 0 else False

def main():
    num=int(input("Enter number: "))  
    
    ret = isDivisibleByFive(num)

    print(f"Input : {num}                Output : {ret}")
    

if __name__ == "__main__":
    main()    