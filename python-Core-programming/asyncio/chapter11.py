# https://www.liaoxuefeng.com/wiki/1016959663602400/1017985577429536 aiohttp介绍
import asyncio
import aiohttp

from bs4 import BeautifulSoup

header = {
    'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control':' max-age=0',
    'Connection':' keep-alive',
    'Cookie':' bid=6g5nTcmo4u0; douban-fav-remind=1; __utmz=30149280.1572568141.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.770658902.1568870221.1572568141.1573023022.3; __utmb=30149280.0.10.1573023022; __utmc=30149280; __utma=223695111.1482886726.1573023022.1573023022.1573023022.1; __utmb=223695111.0.10.1573023022; __utmc=223695111; __utmz=223695111.1573023022.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=3a686c23ce0426a2.1573023022.1.1573023022.1573023022.; _pk_ses.100001.4cf6=*; ap_v=0,6.0',
    'Host':' movie.douban.com',
    'Upgrade-Insecure-Requests':' 1',
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
async  def fetch_content(url):
    async def fetch_content(url):
        async with aiohttp.ClientSession(
                headers=header, connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            async with session.get(url) as response:
                return await response.text()

async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')
    movie_names, urls_to_fetch, movie_dates = [], [], []
    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')
        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)
    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')
        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

asyncio.run(main())