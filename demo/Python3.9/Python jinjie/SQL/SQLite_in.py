import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user(id, name) values (\'1\', \'Michael\')')
# cursor.rowcount
# cursor.close()
# conn.commit()
# conn.close()


# cursor.execute('select * from user where id=?', ('1', ))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

# cursor.execute('alter table user add score int')
# cursor.close()
# conn.close()

# cursor.execute('update user set score = 56 where id=?', ('1', ))
# cursor.execute('insert into user values (\'2\', \'Jock\', 78)')
# cursor.execute('insert into user values (\'3\', \'lisa\', 92)')
# cursor.close()
# conn.commit() #提交事务
# conn.close()


# cursor.execute('select * from user')
# values = cursor.fetchall()
# print(values)
# print(type(values))
# cursor.close()
# conn.close()

# cursor.execute('insert into user values (\'4\', \'xxx\', 66)')
# cursor.close()
# conn.commit() #提交事务
# conn.close()

# cursor.execute('select * from user')
# values = cursor.fetchall()
#
# def get_score_in(low, high):
#     values1 = reversed(sorted(values, key=lambda x: x[-1]))
#     l = []
#     for i in values1:
#         if i[-1] > low and i[-1] < high:
#             l.append(i[1])
#     return l
# assert get_score_in(0, 60) == ['Michael']
# assert get_score_in(60, 80) == ['Jock', 'xxx']
# assert get_score_in(60, 100) == ['lisa', 'Jock', 'xxx']
# print(get_score_in(60, 100))
# cursor.close()
# conn.close()

