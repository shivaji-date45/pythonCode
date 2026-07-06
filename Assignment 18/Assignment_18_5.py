# Write a program which accept N numbers from user and store it into List. 
# Return addition of all prime numbers from that List. Main python file accepts N numbers
# from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime()
from MarvellousNum import ChkPrime
def ListPrime(l1):
    
    sum=0

    for num in l1:
        if ChkPrime(num) == True:
            sum += num
    return sum

def main():
    num=int(input("Number of elements: "))
    
    l1=list()

    for i in range(num):
        l1.append(int(input()))
    
    ret=ListPrime(l1)

    print("Addition of prime number is: ", ret)
    
if __name__ == "__main__":
    main()