# Write a lambda function using filter () which accepts a list of strings
# and returns list of strings having lenght greater than 5
greaterThan5 = lambda a : len(a) > 5  

def main():   
    Data=["fsdfds","fs","fsfdsfsdf","abc"]
    filterData = list(filter(greaterThan5,Data))
    print("strings length greater than 5 are :",filterData)
    
if __name__ == "__main__":
    main()    