import os, sqlite3
import numpy as np
db_file = os.path.join(os.path.dirname(__file__), 'test1.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select id from user where score between ? and ? ',(low,high))
    values = cursor.fetchall()
    print(values)
    print(values[0][0])
    scores = np.zeros(len(values),np.int)
    # cursor.close()
    # cursor = conn.cursor()
    for i in range(len(values)):
        cursor.execute('select score from user where id=?',(values[i][0],))
        scores[i] = cursor.fetchall()[0][0]
    cursor.close()
    order = np.argsort(scores)
    score = scores[np.argsort(scores)]
    id = []
    for i in range(len(values)):
        id.append(values[order[i]][0])
    b=score[0]
    name = []
    cursor = conn.cursor()
    for i in range(len(values)):
        cursor.execute('select name from user where score=?',(score[i],))
        names = cursor.fetchall()
        a = names
        name.append(names[0][0])
    cursor.close()
    conn.close()
    print(name)







if __name__ == '__main__':
    get_score_in(80,95)
    # conn = sqlite3.connect(db_file)
    # cursor = conn.cursor()
    # cursor.execute('select ')
