# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02 创建TCP服务器-client
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
res = s.send(b'Hello')
print(res)
print(s.recv(8192))