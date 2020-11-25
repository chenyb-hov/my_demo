from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write("  "))
print(f.write('StringIO'))
print(f.getvalue())

f = StringIO('Hello\nmick\nseeyou')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
print(f.write('汉字'.encode('utf-8')))
print(f.getvalue())

f = BytesIO(b'\xe6\xb1\x89\xe5\xad\x97')
print(f.read())

