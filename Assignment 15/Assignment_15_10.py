# Write a lambda function using filter () which accepts a list of numbers
# and returns count of even number

even = lambda no: no%2==0

def main():   
    Data=[2,4,5,6,7,11,8,12]
    count = len(list(filter(even  ,Data)))
    print("Count of even numbers in list :",count)
    
if __name__ == "__main__":
    main()    