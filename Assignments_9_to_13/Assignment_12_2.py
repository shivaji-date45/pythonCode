# Write a program which accepts one number 
# and prints its factors

def getAllFactorsOfNumber(No):
    factors = list()
    
    for i in range(1,No+1):
        if No%i==0:
            factors.append(i)
    return factors

def main():
    No=int(input("Enter number: "))
    
    allFactors=getAllFactorsOfNumber(No)

    print(allFactors)

if __name__ == "__main__":
    main()    