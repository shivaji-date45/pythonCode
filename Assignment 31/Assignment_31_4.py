#  Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.
#  Write the result into: DirectoryCountLog.txt
#  Each entry should contain:
#  .Directory path
#  .Number of files
#  .Date and time


import schedule
import time
from datetime import datetime
import os

def countNumberOfFilesInDir(path):

    ret = os.path.exists(path)

    if ret == False:
        print("Path not exists:")
        return

    ret = os.path.isdir(path)

    if ret == False:
        print("Path is not directory !!")
        return

    numberOfFiles=0
    dirPath=""

    for folder,SubFolder,FileName in os.walk(path):
        numberOfFiles = len(FileName)
        dirPath = os.path.realpath(path)

    currentTime=datetime.now()

    fObj = open("DirectoryCountLog.txt","a+")

    currentTime = currentTime.strftime("%d-%m-%Y %I:%M:%S %p")

    fObj.write("Directory path: "+ dirPath+"\n")
    fObj.write("Number of files: "+ str(numberOfFiles)+"\n")
    fObj.write("Date and time: "+str(currentTime)+"\n")

    fObj.close()
    

def main():
    dirName = input("Enter Dir Name: ")

    schedule.every(5).minutes.do(countNumberOfFilesInDir,dirName)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()