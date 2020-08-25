import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',

}
res = requests.get(url="http://www.porters.vip/verify/uas/index.html",headers=headers)
print(res.text)