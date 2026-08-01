# Write a script that schedules the following tasks:
# Print Lunch Time! every day at 1:00 PM.
# Print Wrap up work every day at 6:00 PM.
# Both tasks should be handled by separate functions.

import schedule
import  datetime
import time

def DisplayLunch():
    print("Lunch Time!")

def DisplayWrapUpWork():
    print("Wrap up work")

def main():

    schedule.every().day.at("13:00").do(DisplayLunch)
    schedule.every().day.at("18:00").do(DisplayWrapUpWork)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()