from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])
print(Circle)

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('e')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print((od))

od1 = OrderedDict()
od1['z'] = 1
od1['y'] = 2
od1['x'] = 3
print(list(od1.keys()))

class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove: ', last)
        if containsKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))
        OrderedDict.__setitem__(self, key, value)

defaults = {
    'color': 'red',
    'user': 'guest'
}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
print(defaults['color'])
print(defaults['user'])
dict1 = dict([('x', 11), ('y', 22), ('z', 33)])
print(dict1['x'])
print(defaults)
print(dict1)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
c.update('hello')
print(c)
print(['1', '2', '1', '3', '1'].count('1'))
print(list('123456'))