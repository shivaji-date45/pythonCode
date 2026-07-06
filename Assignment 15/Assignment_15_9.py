# Write a lambda function using reduce () which accepts a list of numbers
# and returns products of all numbers
from functools import reduce

product = lambda no1,no2 : no1*no2

def main():   
    Data=[3,5,3,5,6]
    prod = reduce(product  ,Data)
    print("Product of all elements is :",prod)
    
if __name__ == "__main__":
    main()    