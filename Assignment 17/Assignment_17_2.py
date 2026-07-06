# Write program which accept one number and display belwo pattern
# Input: 5
# Output:
#        * * * * *
#        * * * * *
#        * * * * *
#        * * * * *
#        * * * * *

def PrintPattern(num):
    print("\n")
    for i in range(num):
        for j in range(num):
            print("*",end=" ")
        print("\n")

def main():   
   num=int(input("Enter number: "))
   PrintPattern(num)

if __name__ == "__main__":
    main()    