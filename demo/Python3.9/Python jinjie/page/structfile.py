import struct

n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >>16
b3 = (n & 0xff00) >>8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

print(struct.pack('>I', 10240099))
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
t = struct.unpack('<ccIIIIIIHH', b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00')
print(t)
print(type(t),t[-1],t[-3],t[-4])