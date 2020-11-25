import os
print(os.name)
#windows不支持
#print(os.uname())

# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.environ.get('x', 'default'))
# print(os.path.abspath('.'))
# print(os.path.join('E:/Pytharm/Python jinjie'), 'newdir')
# os.mkdir('E:/Pytharm/Python jinjie/newdir')
# os.rmdir('E:/Pytharm/Python jinjie/newdir')
# print(os.path.split('E:/Pytharm/Python jinjie/mypy.py'))
# os.rename('a.txt', 'a.py')
# os.remove('a.py')
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])