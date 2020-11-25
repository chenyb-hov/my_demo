import pickle
import json
# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))
# f = open('D:/Users/season/Desktop/pyfile.txt', 'wb')
# print(pickle.dump(d, f))
# f.close()
fileurl = 'D:/Users/season/Desktop/pyfile.txt'
f = open(fileurl, 'rb')
d = pickle.load(f)
f.close()
print(d)

d = dict(name='某陈', age=18, gender=1)
print(json.dumps(d, ensure_ascii=True))
print(d)
# 字符串转json 注:单引号套双引号
json_str = '{"name":"cmy", "age":18, "score":66}'
# json_str = "{'name':'cmy', 'age':18, 'score':66}"
print(json.loads(json_str))

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def person_dict(self):
        return {'name': self.name, 'age': self.age, 'gender': self.gender}
# def person_dict(json):
#     return {'name': json.name, 'age': json.age, 'gender': json.gender}
#
# person = Person('hhh', 18, 1)
# print(json.dumps(person, default=person_dict))
print(json.dumps(Person('hhh', 18, 1), default=Person.person_dict))
print(json.dumps(Person('hhh', 18, 1), default=lambda obj: obj.__dict__))

json_str1 = '{"age": 20, "name": "cbb", "gender": 1}'
print(json.loads(json_str1, object_hook=lambda obj: Person(obj['name'], obj['age'], obj['gender'])))