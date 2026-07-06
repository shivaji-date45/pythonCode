# Write a lambda function using reduce () which accepts a list of numbers
# and returns list of numers  divisible by both 3 and 5

divisible = lambda no : (no%3==0) and (no%5==0)

def main():   
    Data=[3,5,15,20,30,27]
    filterData = list(filter(divisible  ,Data))
    print("numbers divisble by 3 and 5 :",filterData)
    
if __name__ == "__main__":
    main()    