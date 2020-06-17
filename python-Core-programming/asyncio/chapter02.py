import asyncio

# 利用协程

import time
import asyncio
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    start = time.time()
    for url in urls:
        await crawl_page(url)
    end = time.time()
    print(end-start)



print(asyncio.run(main(['url_1','url_2','url_3','url_4'])))


# crawling url_1
# OK url_1
# crawling url_2
# OK url_2
# crawling url_3
# OK url_3
# crawling url_4
# OK url_4
# 10.00059986114502
# None