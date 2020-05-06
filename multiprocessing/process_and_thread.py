import time
from multiprocessing import Process, Pool
import threading


def cal(nums):
    count = 0
    for k in range(nums):
        count += k
    return count


def operation_io():
    time.sleep(3)
    print('sleeping')


def one_process_threads():
    l = []
    for i in range(1, 100):
        for j in range(5000, 6000):
            p_thread = threading.Thread(target=cal, args=(j,))
            l.append(p_thread)
    t3 = time.time()
    for t in l:
        t.start()
    t.join()
    return time.time() - t3

def mul_process_mul_threads(nums):
    l = []
    for i in range(1, nums):
        for j in range(5000, 6000):
            p_thread = threading.Thread(target=cal, args=(j,))
            l.append(p_thread)
    t3 = time.time()
    for t in l:
        t.start()
    t.join()
    return time.time() - t3

def mul_process_mul_threads_1():
    l = []
    for j in range(5000, 6000):
        p_thread = threading.Thread(target=cal, args=(j,))
        l.append(p_thread)
    t3 = time.time()
    for t in l:
        t.start()
    t.join()
    return time.time() - t3


if __name__=='__main__':
    print('-----calculation based situation-----')
    print('-------------origin cal-------------')
    t1 = time.time()
    for i in range(1, 100):
        for j in range(5000, 6000):
            count = cal(j)
    print(count)
    print('origin cal time is: %s' %(time.time() - t1))
    print('-------------End of orginal cal--------------')
    ## output>>
    # origin cal time is: 26.91621708869934

    # print('----------one process mul thread-------------')
    # t2 = time.time()
    # p = Pool(1)        
    # alist = []
    # alist.append(p.apply_async(one_process_threads, args=()))
    # p.close()
    # p.join()
    # tt = alist[0].get()
    # print('one process and mul threads cal time is %s' %(time.time() - t2))
    # print('one process and mul threads cal time without creation is %s' %(tt))

    # print('----------End of one process mul thread-------------')
    ## output>>
    # one process and mul threads cal time is 34.39821481704712
    # one process and mul threads cal time without creation is 32.67923879623413


    # print('---------- mul thread-------------')
    # t3 = time.time()      
    # l = []
    # for i in range(1, 100):
    #     for j in range(5000, 6000):
    #         p_thread = threading.Thread(target=cal, args=(j,))
    #         l.append(p_thread)

    # for t in l:
    #     t.start()
    # t.join()
    # print('mul threads cal time is %s' %(time.time() - t3))

    # print('----------End of mul thread-------------')

    ## output>>
    # mul threads cal time is 33.004802227020264



    # print('---------- mul process-------------')
    # t4 = time.time()   
    # p = Pool(4)   
    # l = []
    # for i in range(1, 100):
    #     for j in range(5000, 6000):
    #         l.append(p.apply_async(cal, args=(j,)))


    # p.close()
    # p.join()
    # print('mul process cal time is %s' %(time.time() - t4))

    # print('----------End of mul process-------------')


    ## output>>
    # mul process cal time is 10.585372924804688


    print('---------- mul process mul thread-------------')
    t5 = time.time()   
    p = Pool(4)   
    l = []
    # mul_process_mul_threads  time = 37.703373193740845
    # a = [25, 50, 75, 100]
    # for i in range(4):
    #     l.append(p.apply_async(mul_process_mul_threads, args=(a[i],)))
    for i in range(1, 100):
        l.append(p.apply_async(mul_process_mul_threads_1))
    p.close()
    p.join()
    # tt = ['0'] * 4
    # for i in range(4):
    #     tt[i] = l[i].get()
    print('mul process mul thread cal time is %s' %(time.time() - t5))

    print('----------End of mul process mul thread-------------')

    ## output>>
    # mul process mul thread cal time is 11.297631025314331


    





