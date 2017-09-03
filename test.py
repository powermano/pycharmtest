import tensorflow as tf
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import re
# a=tf.constant("hello world")
# sess=tf.Session()
# print(sess.run(a))

#
# m=re.search(r'\bthe','bite the dog')
# if m is not None:
#    print( m.group())



m=re.findall(r'(th\w+) and (th\w+)','this and that......')
if m is not None:
   for each in m:
       print(each)


regex=re.compile('#([\d,]+) in Books ')
s='#123,456 in Books'
final=regex.findall(s)

#from multiprocessing import Pool
# import os, time, random
# from multiprocessing import Process
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

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

#
# from time import sleep, ctime
# def loop():
#     print('start loop 0 at', ctime())
#     sleep(4)
#     print('loop 0 done at', ctime())
#
# def loop1():
#     print('start loop 1 at', ctime())
#     sleep(2)
#     print('loop 1 done at', ctime())
#
# def main():
#     print('starting at:', ctime())
#     loop()
#     loop1()
#     print('all done at:', ctime())
#
# if __name__=='__main__':
#     main()
