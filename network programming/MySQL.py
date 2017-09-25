#sqlite3 编程
# import os, sqlite3
# import numpy as np
# db_file = os.path.join(os.path.dirname(__file__), 'test1.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)
#
# # 初始数据:
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
# cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
# cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
# cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
# cursor.close()
# conn.commit()
# conn.close()
#
# def get_score_in(low, high):
#     ' 返回指定分数区间的名字，按分数从低到高排序 '
#     conn = sqlite3.connect(db_file)
#     cursor = conn.cursor()
#     cursor.execute('select id from user where score between ? and ? ',(low,high))
#     values = cursor.fetchall()
#     print(values)
#     print(values[0][0])
#     scores = np.zeros(len(values),np.int)
#     # cursor.close()
#     # cursor = conn.cursor()
#     for i in range(len(values)):
#         cursor.execute('select score from user where id=?',(values[i][0],))
#         scores[i] = cursor.fetchall()[0][0]
#     cursor.close()
#     order = np.argsort(scores)
#     score = scores[np.argsort(scores)]
#     id = []
#     for i in range(len(values)):
#         id.append(values[order[i]][0])
#     b=score[0]
#     name = []
#     cursor = conn.cursor()
#     for i in range(len(values)):
#         cursor.execute('select name from user where score=?',(score[i],))
#         names = cursor.fetchall()
#         a = names
#         name.append(names[0][0])
#     cursor.close()
#     conn.close()
#     print(name)
#
# if __name__ == '__main__':
#     get_score_in(80,95)
#     # conn = sqlite3.connect(db_file)
#     # cursor = conn.cursor()
#     # cursor.execute('select ')

import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",port=3306,user= "root", password="123456", db='test')

# cursor = db.cursor()
#
# #创建数据库
# cursor.execute('create database test')
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
#
# db.commit() #必须要确认

# cursor.close()

cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute('select * from user where id = %s', ['1',])

values = cursor.fetchall()#取所有数据

data = cursor.fetchone()# 使用 fetchone() 方法获取单条数据

print("Database version : %s " % 5.7)
print(data)
print(values[0])
cursor.close()
# 关闭数据库连接
db.close()