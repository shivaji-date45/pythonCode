# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 
# and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

filterFun =lambda No1:  No1 >= 70 and No1<= 90

mapFun= lambda No: No+10

reduceFun =  lambda No1,No2 : No1*No2

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