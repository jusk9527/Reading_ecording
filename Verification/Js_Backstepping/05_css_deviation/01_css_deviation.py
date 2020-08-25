import requests
from scrapy import Selector
import  re

url = 'http://www.porters.vip/confusion/flight.html'
response = requests.get(url)
html = Selector(text=response.text)
ems = html.xpath('//em[@class="rel"]').extract()
#每个em标签在循环
for em in ems:
    html_em_element = Selector(text=em)
    html_bs= html_em_element.xpath('//b').extract()
    b_first  = html_bs.pop(0)
    html_b_first = Selector(text=b_first)
    base_price = html_b_first.xpath('//i/text()').extract()
    real_prices = []
    for  html_b_next in  html_bs:
        location = re.search('left:(.*?)px', html_b_next, re.S).group(1)
        price = re.search('">(.*?)</b>', html_b_next, re.S).group(1)
        real_prices.append({'location': location, 'price': price})
    for real_price in real_prices:
       location  = real_price.get('location')
       price = real_price.get('price')
       index = int(int(location)/16)
       base_price[index] = price
    print(base_price)


"""
<em class="rel">
<b style="width:64px;left:-64px">
<i style="width: 16px;">8</i>
<i style="width: 16px;">3</i>
<i style="width: 16px;">9</i>
<i style="width: 16px;">5</i>
</b>
<b style="width: 16px;left:-32px">0</b>
<b style="width: 16px;left:-48px">7</b>
<b style="width: 16px;left:-16px">5</b>
</em>
"""



