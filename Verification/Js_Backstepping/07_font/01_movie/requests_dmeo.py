import requests,re

from fontTools.ttLib import TTFont
from io import BytesIO

from lxml import etree


# 这篇案例的编码是固定的,所以我们只需要在FontCreator中获取的映射关系即可
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

# 手动将从FontCreator中获取的映射关系对应起来


relation_table = {'uniE9C7': '7', 'uniF57B': '1', 'uniE7DF': '2', 'uniE339': '6', 'uniE624': '9', 'uniEA16': '5',
                  'uniF19A': '3', 'uniEE76': '0', 'uniF593': '4', 'uniEFD4': '8'}

def woff_font(woff_url):
    # 发送请求，获取相应
    response = requests.get(woff_url)
    woff_data = BytesIO(response.content)
    # woff 数据读取出来
    font = TTFont(woff_data)
    # 将读取出来的woff数据转为映射关系
    cmap = font.getBestCmap()
    font.close()
    return cmap


# 这里我们就不下载文件了，直接通过访问这个网址拿到woff文件中的数据
woff_url = 'http://www.porters.vip/confusion/font/01_movie.woff'
font_map = woff_font(woff_url)

print(font_map)

# 打印结果：（这里显示的是10进制与编码的映射管辖）
# {120: 'x', 58169: 'uniE339', 58916: 'uniE624', 59359: 'uniE7DF', 59847: 'uniE9C7',
# 59926: 'uniEA16', 61046: 'uniEE76',61396: 'uniEFD4', 61850: 'uniF19A',
# 62843: 'uniF57B', 62867: 'uniF593'}

# 从font_map中将不需要的映射关系删除
newmap = {}
for index, key in enumerate(font_map):
    value = font_map[key]
    # hex() 函数用于将10进制整数转为16进制，以字符串形式表示
    key = hex(key).replace('0', '&#')

    # 为防止对关系中没有相应的value导致报错，这里捕捉下异常
    try:
        # 这里用
        get_real_data = relation_table[value]

    except:
        get_real_data = ''

    if get_real_data != '':
        # 这里我们字体文件中得到的编码字符和真是结果对应起来
        newmap[key] = get_real_data

print(newmap)

# 打印结果：(这个也就是网页中编码与真实结果对应的关系)

# {'&#xe339': '6', '&#xe624': '9', '&#xe7df': '2', '&#xe9c7': '7', '&#xea16': '5',
#'&#xee76': '0', '&#xefd4': '8', '&#xf19a': '3', '&#xf57b': '1', '&#xf593': '4'}

url = 'http://www.porters.vip/confusion/01_movie.html'
reponse_html = requests.get(url, headers=headers).text

# 这里直接在html页面使用正确数据将这些乱码或者编码替换掉
for i in newmap:
    check_html = re.search(i, reponse_html)
    if check_html != None:
        reponse_html = re.sub(i, newmap[i], reponse_html)
# 这个时候可以使用正则或则Xpath（自己喜欢获取数据的方式）获取数据就行了
html = etree.HTML(reponse_html)
# 通过Xpath拿到数据
user_grade = html.xpath('//span[contains(@class,"info-num")]/span/text()')[0].strip()
user_grade_count = html.xpath('//span[@class="score-num"]//span/text()')[0].strip()
box_office_count = html.xpath('//span[contains(@class,"unit")]/preceding-sibling::span/text()')[0].strip()
print('用户评分：' + user_grade, '\n' + user_grade_count + '评分', '\n累积票房:' + box_office_count)

# 打印结果：
"""
用户评分：9.7 
477.9万评分 
累积票房:56.83
"""
