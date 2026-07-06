# Write a lambda function using filter () which accepts a list of numbers
# and returns a list of even numebr

even = lambda a : a%2==0   

def main():   
    Data=[13,12,8,10,11,20]
    filterData = list(filter(even,Data))
    print("Even of Data using filter is :",filterData)
    
if __name__ == "__main__":
    main()    