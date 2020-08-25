# 豆瓣协程爬虫
import time
import requests
from bs4 import BeautifulSoup
def main():
    start = time.time()
    url = "https://01_movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url).content
    init_soup = BeautifulSoup(init_page, 'lxml')
    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')
        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text
        response_item = requests.get(url_to_fetch).content
        soup_item = BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')
        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))
    end = time.time()
    print(end-start)

if __name__ == "__main__":
    main()


# 越域重生 11月07日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2566472233.jpg
# 那座桥 11月07日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572341522.jpg
# 决战中途岛 11月08日 https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2572310947.jpg
# 宠物联盟 11月08日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572918825.jpg
# 受益人 11月08日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572429001.jpg
# 我的拳王男友 11月08日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2571578255.jpg
# 武林孤儿 11月08日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572510173.jpg
# 订亲 11月08日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572745440.jpg
# 黄花塘往事 11月08日 https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2571677229.jpg
# 剩女觅爱记 11月08日 https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2533538748.jpg
# 一个人的城市 11月08日 https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2572417149.jpg
# 爱情图鉴之暗恋 11月08日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572233002.jpg
# 小心“陷阱” 11月08日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572067945.jpg
# 致敬英雄 11月09日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2569122984.jpg
# 搭秋千的人 11月10日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2541748394.jpg
# 他们已不再变老 11月11日 https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2570972919.jpg
# 柬爱 11月11日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2573475685.jpg
# 小轿车 11月12日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572044721.jpg
# 海上钢琴师 11月15日 https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2572390547.jpg
# 盗梦特攻队 11月15日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572953751.jpg
# 霹雳娇娃 11月15日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2572654905.jpg
# 麦子的盖头 11月15日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2531213712.jpg
# 长安道 11月15日 https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2567011046.jpg
# 大约在冬季 11月15日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2571186630.jpg
# 那一夜，我给你开过车 11月15日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2569020564.jpg
# 萌宠特工队 11月15日 https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2569496016.jpg
# 父子拳王 11月15日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2571788322.jpg
# 撼山瑶 11月15日 https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2568504230.jpg
# 19.30840015411377

