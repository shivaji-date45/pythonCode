# Write a lmbda function using map () which accepts a list of numbers
# and returns a list of square of each numebr

sqaureLmbda = lambda a : a*a   

def main():   
    Data=[13,12,8,10,11,20]
    mapData = list(map(sqaureLmbda,Data))
    print("Square of Data using map is :",mapData)
    
if __name__ == "__main__":
    main()    