from multiprocessing import Process
import os

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

#threading model: way 1
# import threading
# from time import ctime, sleep
# loops=[4,2]
# def loop(name,sec):
#     print('loop %d start at:%s' %(name, ctime()))
#     sleep(sec)
#     print('loop %d end at %s' %(name, ctime()))
#
# def main():
#     print('starting at %s' %ctime())
#     threads=[]
#     nloops=range(len(loops))
#     for i in nloops:
#         t=threading.Thread(target=loop,args=(i,loops[i]))
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     print('all done %s' %ctime())
#
# if __name__=='__main__':
#     main()



