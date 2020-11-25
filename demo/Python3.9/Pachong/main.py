# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("start "+self.name)
        print_time(self.name, self.counter, 5)
        print("exit "+self.name)
def print_time(threadName, delay, counter):
    while(counter):
        if(exitFlag):
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s %s "% (threadName, time.ctime(time.time())))
        counter -= 1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    # 执行run()
    thread1.start()
    thread2.start()
    print('Exiting Main Thread')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
