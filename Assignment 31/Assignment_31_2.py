#  Write a program that scans a specified directory every minute.
#   The task should display:
#       Directory name
#       Number of files
#       Number of subdirectories
#       Date and time of scanning
#   Use the os module.
#   Example output:
#   Directory Scanned: E:/Data
#   Total Files: 15
#   Total Subdirectories: 4
#   Scan Time: 25-07-2026 04:30:00 PM



import schedule
import time
import os

def Display(path):
    ret = os.path.exists(path)

    if (ret) == False:
        print("Path not exists")
        return
    ret = os.path.isdir(path)

    if(ret == False):
        print("Directory not exists")
        return

    totalFile=0
    totalSubfile =0
    for folderName,subFolder,folderName in os.walk(path):
        totalFile =len(folderName)
        totalSubfile = len(subFolder)

    tmStamp=time.ctime()

     # Display results matching the exact format
    print(f"Directory Scanned: {path}")
    print(f"Total Files: {totalFile}")
    print(f"Total Subdirectories: {totalSubfile}")
    print(f"Scan Time: {tmStamp}")


def main():
    path = "D:\\disel"
    schedule.every(1).minute.do(Display,path)

    while True:
        schedule.run_pending()
        time.sleep(2)
if __name__ == "__main__":
    main()