from types import MethodType
from enum import Enum, unique
import mypy

class Demo(object):
    pass
demo = Demo()
demo.name = 'test1'
print(demo.name)

def set_time(self, time):
    self.time = time

demo.set_time = MethodType(set_time, demo)
demo.set_time('2020-11-09')
print((demo.time))

demo1 = Demo()
# demo1.set_time('2020-11-11')
Demo.set_time = MethodType(set_time,Demo)
demo2 = Demo()
demo2.set_time('2020-11-12')
print(demo2.time)

# __slots__ 限制属性
class Test(object):
    __slots__ = ('Scripts', 'Images')
test1 = Test()
# test1.name = 'mytest'
test1.Scripts = 'JavaScript'
print(test1.Scripts)

# 父类属性限制对子类无效
class Childtest(Test):
    pass
child1 = Childtest()
child1.name = 'childname'
print(child1.name)

class scores(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value, int):
            raise ValueError('请输入数字')
        if value < 0 or value > 100:
            raise ValueError("数字超出范围")
        self._score = value
s = scores()
# s.set_score('a')
# s.set_score(101)
s.set_score(99)
print(s.get_score())

class Person(object):

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('请输入数字')
        elif value < 0 or value > 150:
            raise ValueError('请输入正确的年龄')
        self._age = value
p = Person()
# p.age = 'axc'
# p.age = 166
p.age = 18
print(p.age)

# 可读写 只读
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

# 多重继承
class Bird(object):
    pass
class Runnable(object):
    pass
class Mammal(object):
    pass
class Ostrin(Bird, Runnable, Mammal):
    pass

# 定制类
class Superman(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Superman obj name : %s' % self.name
    __repr__ = __str__
print(Superman('Mick'))
super1 = Superman('Chen')
print(super1)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a
for i in Fib():
    print(i)

def __getitem__(self, n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a

Fib.__getitem__ = MethodType(__getitem__, Fib)
fib = Fib()
print(fib[5])

def __getitem__(self, n):
    if isinstance(n, int):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
    if isinstance(n, slice):
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a, b = 1, 1
        L = []
        for x in range(stop):
            if x >= start:
                L.append(a)
            a, b = b, a + b
        return L
Fib.__getitem__ = MethodType(__getitem__, Fib)
fib1 = Fib()
print(fib1[0:7])

class Boy(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        elif attr == 'gender':
            return 'man'
        raise AttributeError('\'Boy\' obj has no attribute %s' % attr)
boy = Boy('Yoq')
print(boy.name)
print(boy.age())
print(boy.gender)
# print(boy.address)

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)

class Computer(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My computer name is '+self.name)
cpt = Computer("waixingren")
cpt()
print(callable(Computer('')))
print(callable(cpt))
print(callable(str))
print(callable([1, 2, 3]))
print(callable(None))

# 枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
day2 = Weekday['Tue']
print(day2)
day3 = Weekday.Wed
print(day3.value)
day4 = Weekday(4)
print(day4)
print(day1 == Weekday.Mon)
print(day1 == Weekday['Mon'])
print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
std = Student('s1', Gender.Male)
print(std.gender == Gender.Male)

myclass = mypy.Myclass()
myclass.put('yb chen')
print(type(mypy.Myclass))
print(type(myclass))

def fn(self, name='python'):
    print('come on %s' % name)

Pycome = type('Pycome', (object,), dict(comeon=fn))
c = Pycome()
c.comeon()
print(type(Pycome))
print(type(c))
print(isinstance(c, object))

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    def __init__(self):
        self.l = []
    def add(self, var):
        self.l.append(var)
    def __call__(self):
        return self.l
def x(self):
    print('1')

L = MyList()
L.add(1)
L.add(2)
print(L)
class MyList1(list, metaclass=ListMetaclass):
    def add(self, var):
        return var
L1 = MyList1()
L1.add(1)
L1.add(2)
print(L1)
# Mylist1 = type('Mylist1', (object, list), dict())
# l1 = Mylist1()
# l1.add(2)
# print(l1)



class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s===>%s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField("password")

user = User(id = 123, name = 'T1', email = '123@qwe.com', password = "wxc")
user.save()
