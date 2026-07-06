# Write a program which display first 10 even numbers on screen
# Output: 2 4 6 8 10 12 14 16 18 20

def PrintFirstTenEvenNumber():  
    print("Output:",end=" ") 
    for i in range (2,21,2):
        print(i,end=" ")

def main():
    PrintFirstTenEvenNumber()

if __name__ == "__main__":
    main()    