# Write a lambda function using filter () which accepts a list of numbers
# and returns a list of odd numbers

odd = lambda a : a%2!=0   

def main():   
    Data=[13,12,8,10,11,20]
    filterData = list(filter(odd,Data))
    print("Odd Data using filter is :",filterData)
    
if __name__ == "__main__":
    main()    