

# 简单的爬虫例子

import time

def crawl_page(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

def main(urls):
    start = time.time()
    for url in urls:
        crawl_page(url)
    end = time.time()

    print(end-start)

print(main(['url_1','url_2','url_3','url_4']))




# crawling url_1
# okurl_1
# crawling url_2
# okurl_2
# crawling url_3
# okurl_3
# crawling url_4
# okurl_4
# 10.019000053405762
# None