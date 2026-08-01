#   Write a program that reads and displays the contents of a specified text file every minute.
#   Handle the following conditions:
#       File does not exist
#       File is empty
#       Permission is denied
#       File cannot be opened

import os
import schedule
import time
import sys

def ReadAndDsiplayFileContent(file):
    ret = os.path.exists(file)

    if ret == False:
        print("File not exists \n")
        return 

    try :
        if(os.path.getsize(file) == 0):
            print("File is empty\n")
            return

        fObj = open(file,"r")
        data=fObj.read()
        print(data)

    except  PermissionError :
        print("Premission is denied:")
    except Exception as e:
        print(f"File can not open due to reason:  {e}")

    

def main():
   
        if len(sys.argv) != 2:
          print("Invalid command line arguments: ")
          return
   
        schedule.every(1).minute.do(ReadAndDsiplayFileContent,sys.argv[1])
   
        try :
          while True:
               schedule.run_pending()
               time.sleep(1)
        except KeyboardInterrupt:
           print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()