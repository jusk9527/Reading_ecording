import asyncio
import types


@asyncio.coroutine
def f():
    yield from asyncio.sleep(3)


@types.coroutine
def g():
    yield from asyncio.sleep(3)


async def h():
    await asyncio.sleep(3)