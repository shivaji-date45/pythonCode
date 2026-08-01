# Write a Python program that performs a file backup every hour.
# The program should:
#   Accept the source file path.
#   Accept the destination directory path.
#   Copy the source file to the destination directory.
#   Add the current date and time to the backup filename.
#   Write the backup operation details into:
#       backup_log.txt
# Example backup filename:
#       Data_25_07_2026_16_30_00.txt
# Example log entry:
#       Backup completed successfully at 25-07-2026 04:30:00 PM
# Use the shutil module for file copying.

import schedule
import shutil
import sys
import os
import  datetime
import time

def validatePaths(srcFilePath,destDir):
        ret = os.path.exists(srcFilePath)
     
        if ret == False:
               print("Source path file invalid\n")
               return False
     
        ret=os.path.exists(destDir)
     
        if ret == False:
             print("Destination Path is invalid\n")
             return False
     
        ret = os.path.isdir(destDir)
     
        if ret==False:
             print("Distination Directory not exists")
             return False

        return True

        
def CopyFile(srcFilePath,destDir):
    ret=validatePaths(srcFilePath,destDir)

    if ret == False:
         return
    logObj = open("backup_log.txt","a")

    tmStamp=time.ctime()
    
    destFileName="Data_%s.log"%tmStamp
    destFileName=destFileName.replace(" ","_")
    destFileName=destFileName.replace(":","_")
    dest_path =  os.path.join(destDir,destFileName)

    shutil.copy2(srcFilePath, dest_path)

    log_time = "%s"%tmStamp #tmStamp.strftime("%d-%m-%Y %I:%M:%S %p")
    log_entry = f"Backup completed successfully at {log_time}\n"

    logObj.write(log_entry)

    logObj.close()

def main():
    if len(sys.argv) == 3:
        schedule.every(60).minutes.do(CopyFile,sys.argv[1],sys.argv[2])
    else:
        print("Invalid number of arguments")

    while True:
        schedule.run_pending()
        time.sleep(100)
        
if __name__ == "__main__":
    main()