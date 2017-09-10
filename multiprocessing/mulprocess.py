# 进程中加入线程 的测试
from multiprocessing import Pool
import os, time, random
import threading

def add1(name):
    name = name + 1
    print('the add1 thread variable is %s'% name)

def add2(name):
    name = name + 3
    print('the add2 thread variable is %s' % name)


def long_time_task(name):
    print('Run task %s (%s)...%s' % (name, os.getpid(),threading.current_thread().name))#也是主线程
    start = time.time()
    print('%s process thread %s is running...' % (os.getpid(),threading.current_thread().name))# 为主线程，只要不是通过thread.Thread()产生的线程，都是主线程，
    other1 = threading.Thread(target=add1,args=(name,))# 否则都是主线程启动的新线程，不过主线程和新线程并没有什么特别的区别
    t = threading.Thread(target=loop,args=(name,), name='LoopThread')
    other2 = threading.Thread(target=add2,args=(name,))   #每个进程中的多个线程分别会拷贝该进程的变量数据，互不影响。
    other1.start()
    other2.start()
    t.start()
    other1.join()
    other2.join()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def loop(name):
    print('process %s thread %s is running...' % (os.getpid(),threading.current_thread().name))#会打印出该线程所属于的进程号os.getpid()
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        print('the variable is %s' % name)
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')