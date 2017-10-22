# from enum import Enum, unique
#
# @unique
# class Weekday(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# day1 = Weekday.Mon
#
# print(day1)
# print(day1.value)
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7


###test the type of the input data
# if __name__=='__main__':
#     a = input('choose the n:')
#     print(a)
#     print(type(a))


## test for read file
# file = open('D:/myFile.txt','r')
# read_file = file.read().strip().split()
# print(read_file)



### test for def __new__():
#
# class A(type):
#     pass
#
#
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(A, name, bases, attrs)
#
#     # def __init__(self):
#     #     print('base class work')
#
# class MyList(list, metaclass=ListMetaclass):
#     # def __init__(self):
#     #     print('it works')
#     pass
#
# L = MyList()
# # L.add(1)
# print(type(L))
