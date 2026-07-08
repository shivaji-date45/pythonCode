# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. 
# Map function will calculate its square. Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

filterFun =lambda No1:  No1%2 == 0

mapFun= lambda No: No**2

reduceFun =  lambda No1,No2 : No1+No2

def main():
    Data=[]
    ele = int(input("How many elements wants to enter into data list : "))

    for i in range(ele):
        Data.append(int(input()))
    
    print("Input List: ",Data)
    
    filterData = list(filter(filterFun,Data))

    print("List after filter : ",filterData)

    mapData = list(map(mapFun,filterData))

    print("List after map : ",mapData)

    redData=reduce(reduceFun,mapData)
    
    print("Output if reduce : ",redData)

if __name__ == "__main__":
    main()