import asyncio
import threading
# @asyncio.coroutine
# def hello():
#     print('hi')
#
#     r = yield from asyncio.sleep(1)
#     print('hello again!')
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


# @asyncio.coroutine
# def hello1():
#     print('hi %s' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('hello %s' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello1(), hello1()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))

    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()