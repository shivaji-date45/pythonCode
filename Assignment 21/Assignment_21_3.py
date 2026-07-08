# Design a Python application where multiple threads update a shared variable.
# 	Use a Lock to avoid race conditions.
# 	Each thread should increment the shared counter multiple times.
# 	Display the final value of the counter after all threads complete execution.


import threading

sharedVar=0

loc = threading.Lock()
def incrementVar(threadName,incremt):
    global sharedVar

    for _ in range(incremt):
        with loc:
            sharedVar+=1

    print(f"{threadName} finished   ")


def main():
    threadCount = 5
    incrementValueByThread=100

    threadList=[]

    for i in range(threadCount):
        threadName=f"thread {i+1}"
        tObj = threading.Thread(target=incrementVar,args=(threadName,incrementValueByThread,))
        threadList.append(tObj)
        tObj.start()

    for tObj in threadList:
        tObj.join()
    
    expValue=threadCount*incrementValueByThread

    print(f"Global count: {sharedVar}")
    print(f"Expected value: {expValue}")
    
    
if __name__ == "__main__":
    main()