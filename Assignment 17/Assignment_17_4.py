# Write program which accept one number from user  and return addition of its factors

def AdditionOfFactors(num):
    add=1
    str1="("

    for i in range(1,num+1):
        add=add+i
        str1+="+"
        str1+=str(i)

    str1+=")"

    str2 = str(add)+"\t\t"+str1
    
    return str2

def main():   
   num=int(input("Enter number: "))
   ret = AdditionOfFactors(num)

   print(f"Input : {num}        Output : {ret}")

if __name__ == "__main__":
    main()    