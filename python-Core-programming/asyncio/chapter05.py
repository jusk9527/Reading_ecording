import time
import asyncio

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():

    start = time.time()


    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')
    end = time.time()
    print(end-start)

print(asyncio.run(main()))


# before await
# worker_1 start
# worker_1 done
# awaited worker_1
# worker_2 start
# worker_2 done
# awaited worker_2
# 3.0106000900268555
# None