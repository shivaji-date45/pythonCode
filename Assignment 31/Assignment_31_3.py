#  Write a program that creates a new log file after every ten minutes.
#      The filename should contain the current date and time.
#       Example: MarvellousLog_25_07_2026_16_30_00.txt
#      The file should contain:
#       Log file created successfully.
#       Creation Time: 25-07-2026 04:30:00 PM



import schedule
import time
from datetime import datetime

def CreateLogFileWithContent():
    currentTime=datetime.now()

    logFileName="Marvellouslog_%s.log"%currentTime.strftime("%d_%m_%Y_%H_%M_%S")

    fObj = open(logFileName,"w")

    fObj.write("Log file created successfully.\n")

    content_time = currentTime.strftime("%d-%m-%Y %I:%M:%S %p")
    
    fObj.write("Creation Time: "+str(content_time))

    fObj.close()
    

def main():
    schedule.every(10).minutes.do(CreateLogFileWithContent)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()