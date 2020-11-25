import time, threading, multiprocessing

def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

# print("thread %s is running..." % threading.current_thread().name)
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print("thread %s ended." % threading.current_thread().name)

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(6666666):
        change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(9,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

def run_thread1(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

# t1 = threading.Thread(target=run_thread1, args=(5,))
# t2 = threading.Thread(target=run_thread1, args=(9,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# def loop1():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop1)
#     t.start()

