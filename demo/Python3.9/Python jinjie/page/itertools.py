import itertools

natuals = itertools.count(1)
for i in natuals:
    print(i)
    if i > 10:
        break

n = itertools.repeat('h',4)
for i in n:
    print(i)

natuals1 = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals1)
print(list(ns))

for j in itertools.chain('abc', '123'):
    print(j)

for key, group in itertools.groupby('knknvvknf'):
    print(key, list(group))

for key, group in itertools.groupby('knknvvknf', lambda v: v.upper()):
    print(key, list(group))


from functools import reduce
def pi(N):
    #' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    pie = itertools.takewhile(lambda x: x < (2 * N), itertools.count(1))
    pie1 = list(filter(lambda x: x % 2 != 0, pie))
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    def f():
        y = [-1]
        def g():
            y[0] *= -1
            return y[0]
        return g

    def f1(x):
        return 4/x
    pie2 = list(map(f1, pie1))
    vb = f()
    ff = [vb() for _ in range(N)]
    # pie11 = [x * y for x in pie2 for y in ff]
    # print(pie2)
    # print(ff)
    # print([pie2[l] * ff[l] for l in range(N)])
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    def adds(m, n):
        return m + n
    # step 4: 求和:
    return reduce(adds, [pie2[l] * ff[l] for l in range(N)])
    #return pie3
print(pi(10))