import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Cookie': 'isfirst=789kq7uc1pp4c',

}
res = requests.get(url="http://www.porters.vip/verify/cookie/content.html",headers=headers)
print(res.text)