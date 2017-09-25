### test for @staticmethod and @classmethod
# class Kls(object):
#     def __init__(self, data):
#         self.data = data
#     def printd(self):
#         print(self.data)
#     @staticmethod
#     def smethod(*arg):
#         print('Static:', arg)
#     @classmethod
#     def cmethod(*arg):
#         print('Class:', arg)


###### test for property
class A(object):
    def __init__(self):
        pass
        self.x = None

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return  self.item

#####you can

a=A()
a.z = 3
# print(a.z)

class A(object):
    def __init__(self):
        pass
        self.x = None

    @property
    def name(self):
        return self.x