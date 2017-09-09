# def gen():
#     value = 0
#     while True:
#         receive = yield value #可以通过send传值进来，赋值给receive 但是每个next()只会执行yield value  并没有赋值给receive
#         if receive == 'e':  #yield value只是打印出value这个值，如果直接receive = yield 那么打印出NONE，每次send的时候
#             break            # 还是会把值传给 receive
#         value = 'got: %s' % receive
#         # print(receive)
#
# g=gen()
# print(g.send(None))
# print(g.send('aaa'))
# print(g.send(3))
# print(g.send('e'))

#result
# 0
# got: aaa
# got: 3
# Traceback (most recent call last):
# File "h.py", line 14, in <module>
#   print(g.send('e'))
# StopIteration

# class strtest:
#     def __init__(self):
#         self.val = 1
#
#     def __str__(self):
#         return str(self.val)
#
#
# if __name__ == "__main__":
#     st = strtest()
#     print(st.__str__())
#     print(str(st))


### yiled from :  example
# def accumulate():    # 子生成器，将传进的非None值累加，传进的值若为None，则返回累加结果
#     tally = 0
#     while True:
#         next = yield
#         if next is None:
#            return tally
#         tally = tally + next
#
#
# def gather_tallies(tallies):    # 外部生成器，将累加操作任务委托给子生成器
#    while 1:
#        tally = yield from accumulate()
#        tallies.append(tally)
#
# tallies = []
# a = accumulate()
# acc = gather_tallies(tallies)
# next(acc)    # 使累加生成器准备好接收传入值
# for i in range(4):
#     acc.send(i)

#acc.send(None)  # 结束第一次累加  lacking this statement,tally can not get the results,so tallies=[]
# print(tallies)
# print(next(a))  #print None  :initilize the generator from the begining(tally=0)
# print(a.send(2)) #print None : because the yiled has noting to print out (next = yield)


####
# def reader():
#     # 模拟从文件读取数据的生成器
#     for i in range(4):
#         yield '<< %s' % i
#
#
# def reader_wrapper(g):
#     # 循环迭代从reader产生的数据
#     for v in g:
#         yield v         #replacing it with 'yield from g' can achieve the same effect
#
# wrap = reader_wrapper(reader()) # wrap is a generator,so using 'for x in wrap' can print the element in it.
# for i in wrap:
#     print(i)
#
# # 结果：
# << 0
# << 1
# << 2
# << 3

class SpamException(Exception):
    pass

def writer():
    while True:
        try:
            w = (yield)
        except SpamException:
            print('***')
        else:
            print('>> ', w)

def writer_wrapper(coro2):
    yield from coro2

w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # "prime" the coroutine
for i in [0, 1, 2, 'spam', 4]:
    if i == 'spam':
        wrap.throw(SpamException)
    else:
        wrap.send(i)

next(wrap)