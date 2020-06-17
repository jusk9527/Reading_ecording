# Task编写协程
import asyncio
import time
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    start = time.time()
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task
    end = time.time()
    print(end-start)

print(asyncio.run(main(['url_1','url_2','url_3','url_4'])))


# crawling url_1
# crawling url_2
# crawling url_3
# crawling url_4
# OK url_1
# OK url_2
# OK url_3
# OK url_4
# 4.0025999546051025
# None