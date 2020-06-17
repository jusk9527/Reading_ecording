# 经典的生产者与消费者模型

import asyncio
import random
import time
async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print('{} put a val: {}'.format(id, val))
        await asyncio.sleep(1)

async def main():
    start = time.time()
    queue = asyncio.Queue()
    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))

    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))
    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)
    end = time.time()

    print(end-start)
print(asyncio.run(main()))


# producer_1 put a val: 2
# producer_2 put a val: 2
# consumer_1 get a val: 2
# consumer_2 get a val: 2
# producer_1 put a val: 8
# producer_2 put a val: 4
# consumer_2 get a val: 8
# consumer_1 get a val: 4
# producer_1 put a val: 1
# producer_2 put a val: 6
# consumer_1 get a val: 1
# consumer_2 get a val: 6
# producer_1 put a val: 3
# producer_2 put a val: 7
# consumer_2 get a val: 3
# consumer_1 get a val: 7
# producer_1 put a val: 2
# producer_2 put a val: 2
# consumer_1 get a val: 2
# consumer_2 get a val: 2
# 10.004199981689453
# None