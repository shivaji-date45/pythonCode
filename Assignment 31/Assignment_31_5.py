#   Write a program that schedules the following messages:
#   Monday at 9:00 AM: Start your weekly goals
#   Wednesday at 5:00 PM: Review your weekly progress
#   Friday at 6:00 PM: Weekly work completed
#   Use:
#   schedule.every().monday.at(...)
#   schedule.every().wednesday.at(...)
#   schedule.every().friday.at(...)

import schedule
import time

def DisplayGoal():
    print("Start your weekly goals")

def DisplayProgress():
    print("Review your weekly progress")


def DisplayCompleted():
    print("Weekly work completed")


def main():

    schedule.every().monday.at("09:00").do(DisplayGoal)
    schedule.every().wednesday.at("17:00").do(DisplayProgress)
    schedule.every().friday.at("18:00").do(DisplayCompleted)

    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == "__main__":
    main()