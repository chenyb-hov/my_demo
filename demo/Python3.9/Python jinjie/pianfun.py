import functools
import os
from collections.abc import Iterable
from collections.abc import Iterator
from functools import reduce
import datetime
import time
import numpy

#偏函数
# print(int('123'))
print(int('123', base=8))
print(int('123', base=16))
print(int('111', base=2))
def int2(x, base=2):
    return int(x, base)
print(int2('111'))
int22 = functools.partial(int, base=2)
print(int22('1001'))
max2 = functools.partial(max, 10)
print(max2(7, 6, 9))

def trim(s):
    s1 = ''
    for i in range(len(s)):
        if s[i] == " ":
            continue
        s1 = s[i:]
        break
    for i in range(len(s1)):
        if s1[-1 - i] == " ":
            continue
        return s1[:len(s1)-i]
    return ''

print(trim('  hello  world  ')=='hello  world')
print(trim('  hello')=='hello')
print(trim('  hello'))
print(trim('  hello  ')=='hello')
print(trim('')=='')
print(trim('    ')=='')

def findMinAndMax(L):
    if len(L) > 0:
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                x = L[i + 1]
                L[i + 1] = L[i]
                L[i] = x
        L1 = [L[0], L[-1]]
        return tuple(L1)
    return (None, None)

def findMinAndMax1(L):
    if len(L) > 0:
        L1 = tuple([min(tuple(L))])
        L2 = tuple([max(tuple(L))])
        return L1 + L2
    return (None, None)

print(list(range(10)))
print([x * x for x in range(10, 2)])
print([x * x for x in range(1, 10, 2)])
print("{},{},{}".format(1, 2, 3))
print([m + n for m in 'abc' for n in 'def'])
print([d for d in os.listdir(".")])
d = {'z': '1', 'x': '2', 'y': '3'}
print([m + '=' + n for m, n in d.items()])
v = ['DSD', 'FFFS', 'ASD']
print([t.lower() for t in v])
print([g for g in range(13) if g % 2 == 0])
print([h if h % 3 == 0 else -h for h in range(11)])
print(isinstance(123, str))
L1 = ['Nsd', 123, 'MNKS', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        #t = b
        #b = a + b
        #a = t
        a, b = b, a + b
        n += 1
    return 'end'

print(fib(8))

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        #t = b
        #b = a + b
        #a = t
        yield b
        a, b = b, a + b
        n += 1
    return 'end'

print(fib1(7))
print(next(fib1(5)))
print(next(fib1(5)))

def odd():
    print('now 1')
    yield 1
    print('now 3')
    yield 3
    print('now 4')
    yield 4
print(next(odd()))

for i in fib1(7):
    print(i)
j = fib1(9)
while (True):
    try:
        x = next(j)
        print('j: ', x)
    except StopIteration as e:
        print("end")
        break

def aa():
    num = [0]
    def b():
        num[0] = num[0]+1
        return num[0]
    return b
x = aa()
print(x())
print(x())

def triangles():
    num = 1
    lists = []
    while (True):
        list = []
        for i in range(num):
            if i == 0 or i == num - 1:
                list.append(1)
                continue
            list.append(lists[-1][i - 1] + lists[-1][i])
        lists.append(list)
        yield list
        num += 1
n=0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 5:
        break

for t in results:
    print(t)

def yhsj(l):
    for i in range(len(l) * 2 - 1):
        p = []
        p1 = []
        p2 = []
        for v in range(len(l[int(i / 2)])):
            if len(p) == 0:
                p.append((len(l) * 2 - 1) - 2 * (len(l[int(i / 2)])) + 1)
                continue
            p.append(p[-1] + 4)
        if i % 2 == 0:
            for j in range(len(l)*4 - 3):
                if i % 2 == 0:
                    if j in p:
                        print(l[int(i/2)][p.index(j)], end='')
                    else:
                        print(" ", end='')
        else:
            for c in range(len(p)):
                p1.append(p[c]-1)
                p2.append(p[c]+1)
            for m in range(len(l) * 4 - 3):
                if i % 2 != 0:
                    if m in p1:
                        print('/', end='')
                        continue
                    if m in p2:
                        print('\\', end='')
                        continue
                    print(' ', end='')
        print()
for i in range(len(results) * 2 - 1):
    for j in range(len(results) * 2 - 1):
        if i % 2 == 0:
            print()

print(results)
yhsj(results)

# 可迭代
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
print(isinstance((i for i in range(10)), Iterable))
print('-------||--------')


print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(123, Iterator))
print(isinstance((i for i in range(10)), Iterator))
print('-------||--------')

print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print([x for x in range(1, 10)])
t = iter(range(2))
print(next(t))
print(next(t))
# print(next(t))
b = iter([1,2,3])
print(next(b))
print('-------||--------')

# 递归
def digui(n):
    if n <= 1:
        return 1
    return n * digui(n - 1)
print(digui(5))

def hnt(n,a,b,c):
    if n == 1:
        print(a+'-->'+c)
        return
    hnt(n - 1, a, c, b)
    hnt(1, a, b, c)
    hnt(n - 1, b, a, c)

hnt(4, 'a', 'b', 'c')
print('-------||--------')

# 高阶函数 map
def f(x):
    return x * x
def normalize(name):
    return name[0].upper() + name[1:].lower()
print(list(map(f, [1, 2, 3, 4])))
print(list(range(10)))
print(list(map(str, [1, 2, 3])))

# 高阶函数 reduce
def adds(x, y):
    return x + y
def prod(L):
    def c(x, y):
        return x*y
    return reduce(c,L)
print(reduce(adds, [1,2,3]))
def str2float(s):
    num = len(s)-1-s.index('.')
    s = s.replace('.', '')
    def a(s):
        try:
            return int(s)
        except:
            return 0
    def b(x, y):
        return x * 10 + y
    return reduce(b, map(a, s))/pow(10, num)

# 高阶函数 filter
def js(x):
    return x % 2 == 1
print(list(filter(js, [1, 2, 3, 4, 5])))
def not_empty(x):
    return x and x.strip()
print(list(filter(not_empty,['a', '', ' ', None, 'b'])))

def ss(l):
    if l < 2 :
        return False
    for i in range(2,int(pow(l,1/2))+1):
        if i != l and l % i == 0:
            return False
    return True
print(list(filter(ss, list(range(1,20)))))
def hws(l):
    for i in range(len(str(l))):
        if str(l)[i] != str(l)[-1-i]:
            return False
    return True

print(list(filter(hws, list(range(1,100)))))
print('-------||--------')

# 高阶函数 sorted
print(sorted([-3, -6, 2, -14]))
print(sorted([-3, -6, 2, -14],key=abs))
print(sorted(['Jan', 'Mick', 'PYTHON'], key=str.lower, reverse=True))
l = [('a', 123), ('x', 55), ('g', 88)]
def akey(l):
    return l[0]
def avalue(l):
    return l[1]
print(sorted(l, key=akey))
print(sorted(l, key=avalue))

# 闭包
def f():
    x = [0]
    def g():
        x[0] += 1
        return x[0]
    return g
y = f()
print(y())
print(y())
print('-------||--------')


# 匿名函数
y = lambda x : x * x
print(y(2))
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
print(y.__name__)

# 装饰器
def now():
    return datetime.date.today()
print(now.__name__,now())

# def log1(func):
#     def wrapper(*args, **kw):
#         print("call %s():" % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log1
def now1():
    print(datetime.date.today())
# now1()
# log1(now1)()

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def now3():
    print('zsq')
log2('hello')(now1)()
print('-------||--------')

