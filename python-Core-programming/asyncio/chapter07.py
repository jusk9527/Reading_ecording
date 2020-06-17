# 给协程限定时间，如果超出就取消

import asyncio
import time
async def worker_1():
    print("worker_1")
    await asyncio.sleep(1)
    return 1

async def worker_2():
    print("worker_2")
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3():
    print("worker_3")
    await asyncio.sleep(3)
    return 3


async def main():
    start = time.time()
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())
    await asyncio.sleep(2)
    task_3.cancel()
    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)
    end = time.time()
    print(end-start)

print(asyncio.run(main()))

# worker_1
# worker_2
# worker_3
# [1, ZeroDivisionError('division by zero'), CancelledError()]
# 2.002000093460083
# None