# class storage(dict):
#     # 通过使用__setattr__, __getattr__, __delattr__
#     # 可以重写dict，使之通过“.”调用
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def __getattr__(self, key):
#         try:
#             return  'getattr work' #self[key]
#         except KeyError:
#             return None
#
#     def __delattr__(self, key):
#         try:
#             del self[key]
#         except KeyError:
#             return None
#
#             # __call__方法用于实例自身的调用
#
#     # 达到()调用的效果
#     def __call__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             return None
#
#
# s = storage()
# s.name = "hello"  # 这是__setattr__起的作用
# print(s.name)
# print(s("name"))  # 这是__call__起的作用
# print(s["name"])  # dict默认行为
# print(s.name)  # 这是__getattr__起的作用
# del s.name  # 这是__delattr__起的作用
# print(s("name"))
# #print(s["name"]) # KeyError: 'name'
# print(s.name)


##__getitem__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f=Fib()
# for v in f:
#     print(v)
print(f[2])
print(f[3])