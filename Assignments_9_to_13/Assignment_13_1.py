# Write a program which accepts lenght and width of rectangle
# and prints area

def GetRectangleArea(width,length):
    return width*length
   

def main():    
    wid=int(input("Enter Width: "))
    len=int(input("Enter length: "))

    print("Area of rectangle is: ",GetRectangleArea(wid,len))

if __name__ == "__main__":
    main()    