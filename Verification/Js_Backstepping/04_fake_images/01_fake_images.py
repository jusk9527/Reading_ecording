import requests
import tesserocr
from PIL import Image
from lxml import  etree
import io

image_base_url = 'http://www.porters.vip/confusion/'

url = 'http://www.porters.vip/confusion/recruit.html'
response = requests.get(url)
html = etree.HTML(response.text)
image_path = html.xpath('//div[@class="left col-md-7"]/table[2]/tr[1]/td[2]/img/@src')[0]
image_url = image_base_url + image_path
image_body = requests.get(image_url).content
image = Image.open(io.BytesIO(image_body))
result = tesserocr.image_to_text(image)
print(result)
