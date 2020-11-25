from contextlib import contextmanager, closing
from urllib.request import urlopen

furl = 'D:/Users/season/Desktop/HTML5.html'
try:

    f = open(furl, 'r', encoding='utf-8')
    print(f.read())
finally:
    f.close()

with open(furl, 'r', encoding='utf-8') as f:
    print(f.read())

class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('Query info about %s' % self.name)

with Query('MyC') as q:
    q.query()

class Query1(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query1(name)
    yield q
    print('End')

with create_query('cyb') as q1:
    q1.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag('div') as cr_div:
    print('hhh')

# 爬网页
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        break
        print(line)

@contextmanager
def closing1(thing):
    try:
        yield thing
    finally:
        thing.close()

with closing1(urlopen('https://www.python.org')) as page1:
    for line in page1:
        print(line)