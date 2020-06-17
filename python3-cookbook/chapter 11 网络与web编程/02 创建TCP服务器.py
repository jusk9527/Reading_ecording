# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02 创建TCP服务器
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想实现一个服务器，通过TCP协议和客户端通信。


## -- 解决方案:创建一个TCP服务器的一个简单方法是使用 socketserver 库。例如，下面是一个简单的应答服务器：

from socketserver import BaseRequestHandler,TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)

        while True:
            msg = self.request.revc(8192)
            if not msg:
                break
            self.request.send(msg)

if __name__ == "__main__":
    serv = TCPServer(('', 20000),EchoHandler)
    serv.serve_forever()

