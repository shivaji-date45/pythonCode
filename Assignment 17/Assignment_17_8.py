# Write program which accept one number and print below pattern
# input : 5
# output: 
#        1  
#        1 2 
#        1 2 3 
#        1 2 3 4 
#        1 2 3 4 5

def printPattern(num):

    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end="\t")
        print("\n")   

def main():   
   num=int(input("Enter number: "))
   printPattern(num)

if __name__ == "__main__":
    main()    