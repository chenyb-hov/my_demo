# import logging
# from functools import reduce
# import pdb
# def foo():
#     r = 1
#     if r == -1:
#         return -1
#     return r
# def bar():
#     r = foo()
#     if r == -1:
#         print('error')
#     else:
#         print('success')
#
# try:
#     print('try...')
#     r = 10/0
#     print('result: ', r)
# except ZeroDivisionError as e:
#     print('except: ', e)
# finally:
#     print('finally...')
# print('end')
# print('----------------------------|--------------------------')
#
# try:
#     print('start')
#     r = 10 / int('a')
#     print('result: ', r)
# except ValueError as e:
#     print('ValueError: ', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError: ', e)
# finally:
#     print('end')
# print('----------------------------|--------------------------')
#
# try:
#     r = 10 / int('a')
# except ValueError as e:
#     print('ValueError: ', e)
# except UnicodeError as e:
#     print('UnicodeError: ', e)
# else:
#     print('other error')
# finally:
#     print('end')
# print('----------------------------|--------------------------')
#
# try:
#     print('start')
#     foo()
# except NameError as e:
#     print('NameError: ', e)
# finally:
#     print('end')
# print('----------------------------|--------------------------')
#
# def foo1(x):
#     return 10 / int(x)
# def bar1(x):
#     return foo1(x) * 2
# def main(x):
#     try:
#         print('start')
#         print(bar1(x))
#     except Exception as e:
#         #logging.exception(e)
#         print('error: ', e)
#     finally:
#         print('end')
# main('a')
# print('----------------------------|--------------------------')
#
# class FooError(ValueError):
#     pass
# def foo2(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
# # print(foo2('0'))
#
# def foo3(x):
#     n = int(x)
#     if n == 0:
#         raise FooError('invalid value: %s' % x)
#     return 10 / n
# def bar3(x):
#     try:
#         print(foo3(x))
#     except Exception as e:
#         print('error is ', e)
# bar3('1')
# print(float('123 '))
#
#
# def str2num(s):
#     try:
#         return int(float(s))
#     except ValueError as e:
#         return e
#     except Exception as e:
#         return e
#
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = list(map(str2num, ss))
#     return reduce(lambda acc, x: acc + x, ns)
#
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)
#
# main()
# print('----------------------------|--------------------------')
#
#
# def foo4(x):
#     n = int(x)
#     assert n != 0, 'n is zero'
#     return 10 / n
# # print(foo4('0'))
#
# def foo5(x):
#     n = int(x)
#     logging.info('n = %d' % n)
#     return 10 / n
# logging.basicConfig(level=logging.INFO)
# # print(foo5('0'))
#
# def foo6(x):
#     n = int(x)
#     pdb.set_trace()
#     return 10 / n
# print(foo6('0'))
# print('----------------------------|--------------------------')


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=="__main__":
    import doctest
    doctest.testmod()


