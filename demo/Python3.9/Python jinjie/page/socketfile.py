import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
#
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
# print(data)
# header, html = data.split(b'\r\n\r\n', 1)
# print(html)
# print(header.decode('utf-8'))
# with open('python.html', 'wb') as f:
#     f.write(html)


# s.connect(('127.0.0.1', 9999))
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarch']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
#
# s.send(b'exit')
# s.close()


s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


for data in [b'Xiaomeng', b'Zhangwei', b'Lihua']:
    s1.sendto(data, ('127.0.0.1', 9998))
    print(s1.recv(1024).decode('utf-8'))

s1.close()
