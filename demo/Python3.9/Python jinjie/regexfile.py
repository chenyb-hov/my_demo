import re

print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}-\d{3,8}$', '010 12345'))
if re.match(r'^\d{3}-\d{3,8}$', '010-12345'):
    print('yes')
else:
    print('not')

print('a b ,,  ;.c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,\;\.]+', 'a b ,,  ;.c'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())

m1 = re.match(r'(\d+)(0*)', '10230000')
print(m1.groups())
m2 = re.match(r'^(\d+?)(0*)$', '10230000')
print(m2.groups())

m3 = re.compile(r'^(\d{3})-(\d{3,8})$')
print(m3.match('101-12345').groups())
print(m3.match('102-12345678').groups())

def name_of_email(addr):
    if re.match(r'^<(\D+)>\s[a-zA-Z0-9.]+|(\S+)@\S+.\S+$', addr).groups()[0]:
        return re.match(r'^<(\D+)>\s[a-zA-Z0-9.]+|(\S+)@\S+.\S+$', addr).groups()[0]
    else:
        return re.match(r'^<(\D+)>\s[a-zA-Z0-9.]+|(\S+)@\S+.\S+$', addr).groups()[1]
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.org'))