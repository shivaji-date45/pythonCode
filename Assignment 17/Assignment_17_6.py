# Write program which accept one number and print below pattern
# input : 5
# output: 
#         * * * * *
#         * * * *
#         * * * 
#         * *
#         *

def printPattern(num):

    for i in range(num):
        for j in range(num-i):
            print("*",end="\t")
        print("\n")   

def main():   
   num=int(input("Enter number: "))
   printPattern(num)

if __name__ == "__main__":
    main()    