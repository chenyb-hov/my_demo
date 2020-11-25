from aiohttp import web
import asyncio

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', headers={'content-type': 'text/html'})

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), headers={'content-type': 'text/html'})

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    # runner = web.AppRunner(app)
    # await runner.setup()
    # site = web.TCPSite(runner, '127.0.0.1', 8887)
    # await site.start()

    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8887)
    print('Server started at http://127.0.0.1:8887....')
    return srv
    # return site

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
#loop.run_until_complete(init())
loop.run_forever()