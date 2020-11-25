'a test module'
__author__ = 'boy Chen'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello mk')
    elif len(args) == 1:
        print('hello %s' % args[1])
    else:
        print('too many arguments')

def __private_1(name):
    return 'hello %s' % name
def _private_2(name):
    return 'hi %s' % name
def greeting(name):
    if len(name) >= 3:
        print(__private_1(name))
        return
    print(_private_2(name))
if __name__ == '__main__':
    test()
    greeting('yb chen')
    print(__private_1("wxc"))