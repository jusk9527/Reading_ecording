import hashlib
import base64
import random
import requests
from datetime import datetime
"""
LV 安卓 app 的请求头的 x-wsse 的生成方法
"""
arg1 = ''
for i in range(10):
    ch = hex(random.randint(0, 0x100))
    arg1 += ch[2:]

print(arg1)
arg2 = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
print(arg2)
arg = arg1 + arg2 + "ks4Cphts57UMNx3H7NBQ3hZj"
data = hashlib.sha512(arg.encode('utf-8')).digest()
data_b64 = base64.b64encode(data).decode()
print(data_b64)

wsse = 'Token created=2019-10-06T15:15:50.995Z,digest={},nonce={}'.format(data_b64, arg1)
print(wsse)
headers = {
    'x-wsse': wsse,
    'User-Agent': 'LVapp/android/5.5 LVApp PRD',
    'Host': 'pass.louisvuitton.com',

}

params = (
    ('locale', 'zh_CN'),
)

response = requests.get('https://pass.louisvuitton.com/api/v5.3/website-cache-catalog', headers=headers, params=params)
print(response.text)