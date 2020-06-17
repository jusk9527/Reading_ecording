# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/9
-------------------------------------------------
   Change Activity:
                   2019/12/9:
-------------------------------------------------
"""

# 作为客户端与HTTP服务交互

## 你需要通过HTTP协议以客户端的方式访问多种服务。例如，下载数据或者与基于REST的API进行交互。
from urllib import request, parse
# GET 请求
url = "http://httpbin.org/get"
parms = {
    "name1":"value1",
    "name2":"value2"
}

querystring = parse.urlencode(parms)
u = request.urlopen(url+'?'+querystring)
resp = u.read()
print(resp)

## b'{\n  "args": {\n    "name1": "value1", \n    "name2": "value2"\n  }, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.6"\n  }, \n  "origin": "183.134.196.227, 183.134.196.227", \n  "url": "https://httpbin.org/get?name1=value1&name2=value2"\n}\n'

# POST请求
from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a POST request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()
print(resp)

## b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "name1": "value1", \n    "name2": "value2"\n  }, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Content-Length": "25", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.6"\n  }, \n  "json": null, \n  "origin": "183.134.196.227, 183.134.196.227", \n  "url": "https://httpbin.org/post"\n}\n'


## 修改 user-agent 字段
from urllib import request, parse
...

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request and read the response
u = request.urlopen(req)
resp = u.read()
print(resp)

## b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {\n    "name1": "value1", \n    "name2": "value2"\n  }, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Content-Length": "25", \n    "Content-Type": "application/x-www-form-urlencoded", \n    "Host": "httpbin.org", \n    "Spam": "Eggs", \n    "User-Agent": "none/ofyourbusiness"\n  }, \n  "json": null, \n  "origin": "183.134.196.227, 183.134.196.227", \n  "url": "https://httpbin.org/post"\n}\n'


# requests 库

import requests

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(url, data=parms, headers=headers)

# Decoded text returned by the request
text = resp.text


## 抓取HTTP头数据

import requests

resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']


## 利用requests通过基本认证登录Pypi
import requests

resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user','password'))

## 利用requests将HTTP cookies从一个请求传递到另一个

import requests

# First request
resp1 = requests.get(url)
...

# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)

## 文件发送
import requests
url = 'http://httpbin.org/post'
files = { 'file': ('data.csv', open('data.csv', 'rb')) }

r = requests.post(url, files=files)


import requests
r = requests.get('http://httpbin.org/get?name=Dave&n=37',
headers = { 'User-agent': 'goaway/1.0' })
resp = r.json
resp['headers']
{'User-Agent': 'goaway/1.0', 'Content-Length': '', 'Content-Type': '',
'Accept-Encoding': 'gzip, deflate, compress', 'Connection':
'keep-alive', 'Host': 'httpbin.org', 'Accept': '*/*'}
resp['args']
{'name': 'Dave', 'n': '37'}