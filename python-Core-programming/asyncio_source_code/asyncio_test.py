import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

loop = asyncio.get_event_loop()
loop.run_until_complete(compute(1, 2))
loop.close()