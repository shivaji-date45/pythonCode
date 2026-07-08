# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).
# 
# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def filterFun(No1):

    for i in range(2,No1):
        if No1 % i == 0:
            return False
        
    return True

def mapFun(No1):
    return No1*2

def reduceFun(No1,No2):
    return No1 if No1 > No2 else No2

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