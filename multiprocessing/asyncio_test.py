# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

import asyncio
import threading
import time

@asyncio.coroutine
def Hello():
    print('Hello,World.(%s),%s'%(threading.currentThread(),time.time()))
    yield from asyncio.sleep(0.00000000000000000001)
    print('Hello again.(%s),%s'%(threading.currentThread(),time.time()))
    print('Goodbye')

loop=asyncio.get_event_loop()
task=[Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello(),Hello()]
loop.run_until_complete(asyncio.wait(task))#运行
loop.close()