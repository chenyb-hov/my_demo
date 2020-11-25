import os
from multiprocessing import Process
#print('Process (%s) start...' % os.getpid())

#Linux/unix/mac
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=="__main__":
#     print("Parent process %s" % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print("Child process will start")
#     p.start()
#     p.join()
#     print("Child process end")

from multiprocessing import Pool
import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print("Task %s runs %0.2f seconds." % (name, (end - start)))
#
# if __name__=="__main__":
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4) # 最大进程同时进行数 默认CPU核数
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print("Waiting for all subprocesses done...")
#     p.close()
#     p.join() # 等待所有进程执行完毕
#     print("All subprocesses done.")

import subprocess

# print("$ nslookup www.python.org")
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('Exit code:', p.returncode)

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=="__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

#在Unix/Linux下，可以使用fork()调用实现多进程。

#要实现跨平台的多进程，可以使用multiprocessing模块。

#进程间通信是通过Queue、Pipes等实现的。