from django.shortcuts import render

# Create your views here.

from django.views import View
import asyncio
import time
from django.http import JsonResponse

class TestAsyncioView(View):
    def get(self, request, *args, **kwargs):
        """
        利用asyncio和async await关键字（python3.5之前使用yield）实现协程
        """
        start_time = time.time()
        loop = asyncio.new_event_loop()  # 或 loop = asyncio.SelectorEventLoop()
        asyncio.set_event_loop(loop)
        self.loop = loop
        try:
            results = loop.run_until_complete(self.gather_tasks())
        finally:
            loop.close()
        end_time = time.time()
        return JsonResponse({'results': results, 'cost_time': (end_time - start_time)})

    async def gather_tasks(self):
        """
         也可以用回调函数处理results
        task1 = self.loop.run_in_executor(None, self.io_task1, 2)
        future1 = asyncio.ensure_future(task1)
        future1.add_done_callback(callback)

        def callback(self, future):
            print("callback:",future.result())
        """
        tasks = (
            self.make_future(self.io_task1, 3),
            self.make_future(self.io_task2, 2)
        )
        results = await asyncio.gather(*tasks)
        return results

    async def make_future(self, func, *args):
        future = self.loop.run_in_executor(None, func, *args)
        response = await future
        return response

    """
    # python3.5之前无async await写法
    import types
    @types.coroutine
    # @asyncio.coroutine  # 这个也行
    def make_future(self, func, *args):
        future = self.loop.run_in_executor(None, func, *args)
        response = yield from future
        return response
    """

    def io_task1(self, sleep_time):
        time.sleep(sleep_time)
        return 66

    def io_task2(self, sleep_time):
        time.sleep(sleep_time)
        return 77