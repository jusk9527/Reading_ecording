import asyncio
import time
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

    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')

    end = time.time()

    print(end-start)


print(asyncio.run(main()))


# before await
# worker_1 start
# worker_2 start
# worker_1 done
# awaited worker_1
# worker_2 done
# awaited worker_2
# 2.0085999965667725
# None

# asyncio.run(main()),程序进入main()函数，事件循环开启
# task1和task2任务被创建，并进入时间循环等待运行，运行到print,输出 'before await'
# await task1执行，用户选择从当前的主任务中切出，时间调度器开始调度worker_1
# worker_1 开始运行，运行print 输出‘worker_2 start’,然后运行await asyncio.sleep(2)从当前任务切出
# 以上所有时间的运行时间，都应该在1ms到10ms之间，甚至可能更短，时间调度器从这个时候开始暂停调度
# 一秒后，worker_1的sleep完成，时间调度器将控制权重新传给task_1,输出‘worker_1 done’,task_1完成任务，从时间循环中退出
# 两秒钟后，worker_2的sleep完成，事件调度器将控制权重新传给task_2, 输出‘worker_2 done’,task_2完成任务，从时间循环中退出
# 主任务输出 ‘awaited worker_2’,协程全人物结束，时间循环结束