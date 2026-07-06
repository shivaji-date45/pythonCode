# Write a lambda function using reduce () which accepts a list of numbers
# and returns minimum element
from functools import reduce
add = lambda ele1,ele2 : ele1 if ele1 < ele2 else ele2

def main():   
    Data=[13,12,8,10,11,20]
    res = reduce(add,Data)
    print("Minimum element is  :",res)
    
if __name__ == "__main__":
    main()    