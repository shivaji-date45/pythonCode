#  Write a program that copies all .txt files from one directory to another every ten minutes.
#  The program should:
#   Accept source and destination directories
#   Validate both directories
#   Copy only .txt files
#   Maintain a log of copied files
#   Avoid terminating if one file cannot be copied


import schedule
import time
import shutil
from datetime import datetime
import sys
import os

def validatePaths(srcDir,destDir):
        ret = os.path.exists(srcDir)
     
        if ret == False:
               print("Source path file invalid\n")
               return False

        ret = os.path.isdir(srcDir)

        if ret == False:
             print("Source Directory not exists")
             return

        ret=os.path.exists(destDir)
     
        if ret == False:
             print("Destination Path is invalid\n")
             return False
     
        ret = os.path.isdir(destDir)
     
        if ret==False:
             print("Distination Directory not exists")
             return False

        return True

def CopyFiles(srcDir,destDir):
    ret = validatePaths(srcDir,destDir)

    if ret == False:
         return

    fObj = open("log.txt","a+")

    for filename in os.listdir(srcDir):

        if filename.endswith(".txt"):
            srcPath=os.path.join(srcDir,filename)
            destPath=os.path.join(destDir,filename)

            if os.path.isdir(srcPath):
                 continue

            try :
                 shutil.copy2(srcPath,destPath)
                 now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
                 fObj.write(f"{filename} from {srcDir} copied to {destDir} at time : {now} \n")

            except Exception as e:
                 fObj.write(f"{filename} from {srcDir} failed to copy {destDir} at time : {now} \n ")
                     
    fObj.close()

def main():

    if (len(sys.argv) != 3):
        print("Invalid command line arguments:")
        return

    schedule.every(10).minutes.do(CopyFiles,sys.argv[1],sys.argv[2])

    while True:
         schedule.run_pending()
         time.sleep(600)
         
if __name__ == "__main__":
    main()