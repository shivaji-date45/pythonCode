# Write a program which accepts one number 
# and check whether it is perfect number or not

def IsNumberPerfectNumber(No):
    ret = False
    sum=0

    for i in range(1,No):
        if ( No % i == 0):
            sum=sum+i

    if ( No == sum):
        ret=True

    return ret
   

def main():    
    No=int(input("Enter Number: "))

    if IsNumberPerfectNumber(No) == True:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()    