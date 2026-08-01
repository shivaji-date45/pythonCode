#  Write a Python program that monitors the size of a specified file every 30 seconds.
#   Write the following details into:
#   FileSizeLog.txt
#       File path
#       File size in bytes
#       Date and time
#   Handle the situation where the file does not exist.


import schedule
import time
from datetime import datetime
import os
import sys


def WriteFile(file):

    ret = os.path.exists(file)

    if ret == False:
        print("File does not exist:")
        return
    
    fObj=open("FileSizeLog.txt","a+")

    path=os.path.realpath(file)
    fsize=os.path.getsize(file)
    dateAndTime=datetime.now().strftime("%d-%m-%Y %I:%M%S %p")

    fObj.write(f"\nFile path: {path} \n")
    fObj.write(f"File size : {fsize}bytes \n")
    fObj.write(f"Date Time : {dateAndTime} \n")

    fObj.close()
    
def main():

    if len(sys.argv) != 2:
       print("Invalid command line arguments: ")
       return

    schedule.every(30).seconds.do(WriteFile,sys.argv[1])

    try :
       while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    main()