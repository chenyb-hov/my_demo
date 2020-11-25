import types

class Cxy(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def print_info(self):
        print("name : %s, age : %s" % (self.__name, self.__age))

cxy1 = Cxy('wxc', 22)
print(cxy1._Cxy__name)
cxy1.print_info()

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def grade(self):
        if self.__score >= 95:
            return 'A'
        elif self.__score >= 80 and self.__score < 95:
            return 'B'
        elif self.__score >= 60 and self.__score < 80:
            return 'C'
        else:
            return 'D'
    def getname(self):
        return self.__name

stu1 = Student('limen', 81)
print(stu1.getname()+' : '+stu1.grade())

class Animal(object):
    def run(self):
        print("animal is run")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
cat1 = Cat()
cat1.run()
class Pink(Animal):
    def run(self):
        print('pink is very low')
pink1 = Pink()
pink1.run()
print(isinstance(pink1, Pink), isinstance(pink1, Animal))
def run_twice(Animal):
    Animal.run()
run_twice(cat1)
run_twice(pink1)
print('--------------------------||-----------------------------')

print(type(cat1))
print(type(123))
print(type('123'))
print(type([1, 2, 3]))
print(type({'a': 1, 'b': 2}))
print(type(None))

def fn():
    pass
print(type(fn))
print(type(lambda x: x) == types.LambdaType)
print(type(lambda x: x))
print(type(abs))
print(type(x for x in range(10)))
print(isinstance([1, 2, 3], (list, tuple)))
print(dir('abc'))
print(len('abc')=='abc'.__len__())

class Len1(object):
    def __len__(self):
        return 1
len1 = Len1()
print(len(len1))

class Myobj(object):
    def __init__(self):
        self.x = 3
        self.y = 4
    def power(self):
        return self.x * self.y
myobj = Myobj()
print(hasattr(myobj, 'x'))
print(myobj.x)
print(hasattr(myobj, 'z'))
setattr(myobj, 'z', 5)
print(myobj.z)
print(getattr(myobj, 'y'))
# print(myobj.v)
print(getattr(myobj, 'y', 404))
print(hasattr(myobj, 'power'))
print(getattr(myobj, 'power'))
print(myobj.power())

def readImage(fp):
    if hasattr(fp, 'read'):
        return fp
    return None

print('--------------------------||-----------------------------')

class User(object):
    __name = 'Username'
    age = 20
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
user = User()
# print(user.__name)
# print(getattr(user, 'name'))
print(user.get_name())
user.set_name("Xiaoming")
print(user.get_name())
user.age = 18
print(user.age)
print(User.age)
del user.age
print(user.age)

class Jishu(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Jishu.count += 1
count1= Jishu('a')
count2= Jishu('b')
print(Jishu.count)

