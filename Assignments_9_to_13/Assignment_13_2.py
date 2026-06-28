# Write a program which accepts radius of circle
# and prints area

def GetCircleArea(rad):
    return 3.14*rad*rad
   

def main():    
    rad=int(input("Enter radious: "))

    print("Area of cicle is: ",GetCircleArea(rad))

if __name__ == "__main__":
    main()    