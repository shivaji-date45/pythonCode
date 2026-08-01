#   Write a program that creates a new text file every minute.
#   The filename should contain the current timestamp.
#   Example:
#   File_25_07_2026_16_30_00.txt
#   Write the following information into the file:
#   Filename
#   Creation date
#   Creation time

import schedule
import time
from datetime import datetime

def WriteIntoFile():
    ctime=datetime.now()
    FileTime=ctime.strftime("%d_%m_%Y_%H_%M_%S")
    filename= f"File_{FileTime}.txt"

    CreationDate=ctime.strftime("%d-%m-%Y")
    CreationTime=ctime.strftime("%I:%M:%S %p") 

    fObj=open(filename,"w")

    fObj.write("\nFilename : "+ filename + "\n")
    fObj.write("Creation date : "+ CreationDate + "\n")
    fObj.write("Creation time : " + CreationTime + "\n")

    fObj.close()


def main():
   schedule.every(1).minute.do(WriteIntoFile)

   while True:
       schedule.run_pending()
       time.sleep(2)

       

if __name__ == "__main__":
    main()