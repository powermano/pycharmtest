# import logging
#
# from time import time
#
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# is_debug = True
#
# def count_time(is_debug):
#     def  handle_func(func):
#         def  handle_args(*args, **kwargs):
#             if is_debug:
#                 begin = time()
#                 func(*args, **kwargs)
#                 logging.debug("[" + func.__name__ + "] -> " + str(time() - begin))
#             else:
#                 func(*args, **kwargs)
#         return handle_args
#     return handle_func
#
# def pr():
#     for i in range(1,100000):
#         i = i * 2
#     print("hello world")
#
# def test():
#     pr()
#
# @count_time(is_debug)
# def test2():
#     pr()
#
# @count_time(False)
# def test3():
#     pr()
#
# # @count_time()
# # def test4():
# #     pr()
#
# # if __name__ == '__main__':
# test()
# test2()
# test3()
# # test4()


# def makeHtmlTag(tag, *args, **kwds):
#     def real_decorator(fn):
#         css_class = " class='{0}'".format(kwds["css_class"]) \
#             if "css_class" in kwds else ""
#
#         def wrapped(*args, **kwds):
#             return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"
#
#         return wrapped
#
#     return real_decorator
#
#
# @makeHtmlTag(tag="b", css_class="bold_css")
# @makeHtmlTag(tag="i", css_class="italic_css")
# def hello():
#     return "hello world"
#####makeHtmlTag(makeHtmlTag(hello))

# print(hello())

#the result
##<b class='bold_css'><i class='italic_css'>hello world</i></b>


##
# class 式的decorator
#
# class myDecorator(object):
#     def __init__(self, fn):
#         print("inside myDecorator.__init__()")
#         self.fn = fn
#
#     def __call__(self):
#         self.fn()
#         print("inside myDecorator.__call__()")
#
#
# @myDecorator
# def aFunction():
#     print("inside aFunction()")
#
#
# print("Finished decorating aFunction()")
#
# aFunction()


#############test for decorator: how to specify an optional argument for a class based or simple decorator
import functools
def log(text=None):
    if callable(text):
        func = text

        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper

    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

@log
def f1():
    print('this is f1')

@log('excute')
def f2():
    print('this is f2')

f1()
f2()

###########test for class based decorator with arguments

# class makeHtmlTagClass(object):
#     def __init__(self, tag, css_class=""):
#         self._tag = tag
#         self._css_class = " class='{0}'".format(css_class) \
#             if css_class != "" else ""
#
#     def __call__(self, fn):
#         def wrapped(*args, **kwargs):
#             return "<" + self._tag + self._css_class + ">" \
#                    + fn(*args, **kwargs) + "</" + self._tag + ">"
#
#         return wrapped
#
#
# @makeHtmlTagClass(tag="b", css_class="bold_css")
# @makeHtmlTagClass(tag="i", css_class="italic_css")
# def hello(name):
#     return "Hello, {}".format(name)
#
#
# print(hello("Hao Chen"))



###########test functools.wraps()
from inspect import getmembers, signature
class test():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def method_test(self, x,y):
        self.m = x
        self.n = y
        return self.m+self.n

    def __call__(self, *args, **kwargs):
        return self.m+self.n

test1 = test(1,2)
print(signature(test1))
print(signature(test1.method_test))
## the result:
# (*args, **kwargs)
# (x, y)


