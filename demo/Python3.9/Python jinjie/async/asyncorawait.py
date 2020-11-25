import asyncio

@asyncio.coroutine
async def hello():
    print('hi!')
    r = await asyncio.sleep(1)
    print('hello')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()