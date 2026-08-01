#   Write a program that deletes all empty files from a specified directory every hour. 
# The program should: 
#   Scan the directory recursively
#   Detect files whose size is zero bytes
#   Delete the empty files
#   Store deleted file paths in a log file
#   Handle permission errors
#   Test the program only on a sample directory.


import schedule
import sys
import os
import time

##################################################################
#
#       Function Name : DirectoryScanner
#       Input :         Name of Directory
#       Description :   Delete all empty files periodically
#       Date:           19/07/2026
#       Author:         Shivaji Ashok Date
##################################################################
def DirectoryScanner(dirPath):
    border="-"*100
    tmStamp=time.ctime()

    logFileName="Marvellouslog%s.log"%tmStamp
    logFileName=logFileName.replace(" ","_")
    logFileName=logFileName.replace(":","_")
    
    #print(logFileName)

    fObj=open(logFileName,"w")

    ret = os.path.exists(dirPath)

    if ret == False:
        print(f"Marvellous automation error: There is no such directory with name {dirPath}")
        return
    
    ret = os.path.isdir(dirPath)

    if ret == False:
        print(f"Marvellous automation error:  {dirPath} is not directory")
        return
    
    fObj.write(border+"\n")
    fObj.write("Marvellous Automation Script: \n")
    fObj.write(border+"\n\n")

    fObj.write("files from the directory are: \n")
    fObj.write(border+"\n")
    
    totalFile=0
    emptyFiles=0
    filePaths=[]

    for folderName,SubFolder,Filename in os.walk(dirPath):     
        for fName in Filename:            
            fName=os.path.join(folderName,fName)
            fObj.write(fName+":\t"+ str(os.path.getsize(fName))+"\n\n")
            totalFile+=1

            if(os.path.getsize(fName) == 0):
                try:
                    os.remove(fName)
                    filePaths.append(fName)
                    emptyFiles+=1
                except PermissionError:
                    print(f"Permission denied for {fName} ")
                except Exception as e:
                    print(f"Error processing file {fName}")

    fObj.write(border+"\n")
    fObj.write("Total files scanned:  "+ str(totalFile)+"\n")
    fObj.write("Total empty files found and deleted:  "+ str(emptyFiles)+"\n")
    fObj.write("Deleted files: \n")

    for path in filePaths:
        fObj.write(fName+"\n")

    fObj.write(border+"\n")
    fObj.write("Log file gets created at: "+tmStamp)
    fObj.write("\n"+border+"\n")

    fObj.close()

##################################################################
#
#       Function Name : DirectoryScanner
#       Input :         Command line argument
#       Description :   It controls the script
#       Date:           19/07/2026
#       Author:         Shivaji Ashok Date
##################################################################

def main():
    border="-"*100
    print(border)
    print("Marvellous Automation Script")
    print(border)


    if len(sys.argv) == 2:
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script use to travel the directory")
            print("For better usage please check --u or --U flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as below:")
            print("python filename.py dir_name")
            print("dir_name should be absolute path")
        else:
            schedule.every(1).hour.do(DirectoryScanner,sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)

        print(border)
        print("Thank you for using Marvellous Automation Script")
        print(border)

   
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u switch for more information")

##################################################################
#   Starter of automation script
##################################################################

if __name__ == "__main__":
    main()