import base64
import struct
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))
print(base64.b64encode(b'abcd'))
print(base64.b64decode(b'YWJjZA=='))
print(base64.b64decode('YWJjZA=='))
# print(base64.b64decode(b'YWJjZA'))
# print(base64.b64decode('YWJjZA'))
a = 'YWJjZA=='
print(type(b'YWJjZA=='),str(b'YWJjZA==')+'=')
c = str(b'YWJjZA=').replace("'", '')[1:]+'='
print(c)
#print(base64.b64decode('YWJjZA='))
def safe_base64_decode(s):
    try:
        return base64.b64decode(s)
    except:
        return safe_base64_decode(str(s).replace("b'", '').replace("'",'')+'=')
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
print(safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA'))

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

def bmp_info(data):
    try:
        x = struct.unpack('<ccIIIIIIHH', bmp_data[0:30])
        if x[0]==b'B' and x[1]==b'M':
            return {
                'width': x[-4],
                'height': x[-3],
                'color': x[-1]
            }
    except:
        return 'not wtpic'