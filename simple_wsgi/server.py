# server.py
# coding: utf-8
""""
1. 初始化，建立套接字
2. 设置加载的web app；
3. 开始持续运行server
4. 处理访问请求，在这里可以加入自己的处理过程，比如我加入了打印访问信息，字典化访问头部信息等功能
5. 获取请求信息及环境信息(get_environ(self))
6. 用environ 运行加载的web app得到返回信息
7. 构造返回信息头部；
8. 返回信息


本质：其实一个 wsgi server 的重要之处就在于用environ去跑 web app 得到返回结果这一步，
这一步和前面的 application 实现相辅相成，然后框架和服务器都根据这套标准，大家就可以愉快的一起工作了
参考连接：
    https://juejin.im/entry/5754ece97db2a20069902655
"""
from __future__ import unicode_literals
import socket
import datetime
import sys
from app import application
from middleware import TestMiddle




class WSGIServer(object):
    request_queue_size = 10

    def __init__(self, address):
        # 初始化
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.socket.bind(address)
        # 监听
        self.socket.listen(self.request_queue_size)

        # 得到host、port
        host, port = self.socket.getsockname()[:2]


        self.host = host
        self.port = port

    def set_application(self, application):
        """
        初始化app
        :param application:
        :return:
        """
        self.application = application



    def handle_request(self):
        """
        处理请求
        :return:
        """
        self.request_data = self.connection.recv(1024)
        self.request_lines = self.request_data.splitlines()
        self.get_url_parameter()
        env = self.get_environ()
        app_data = self.application(env, self.start_response)

        print('[{0}] "{1}" {2}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                 self.request_lines[0], self.status))

        return self.finish_response(app_data)


    def get_url_parameter(self):
        try:
            self.request_dict = {'Path': self.request_lines[0]}
        except Exception as e:
            print(e)
        for itm in self.request_lines[1:]:
            itm = str(itm)
            if ':' in itm:
                self.request_dict[itm.split(':')[0]] = itm.split(':')[1]
        self.request_method, self.path, self.request_version = self.request_dict.get('Path').split()




    def get_environ(self):
        """
        配置一些环境信息
        :return:
        """

        env = {
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            # 'wsgi.input': StringIO.StringIO(self.request_data),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
            'REQUEST_METHOD': str(self.request_method),
            # 'PATH_INFO': self.path,
            'SERVER_NAME': self.host,
            'SERVER_PORT': self.port,
            # 'USER_AGENT': self.request_dict.get('User-Agent')
            'dd': 'xxx',
        }
        return env

    def start_response(self, status, response_headers):
        """
        响应返回的状态及返回头
        :param status:
        :param response_headers:
        :return:
        """
        headers = [
            ('Date', datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')),
            ('Server', 'RAPOWSGI0.1'),
        ]
        self.headers = response_headers + headers
        self.status = status

    def finish_response(self,app_data):
        """
        最后返回响应头和数据
        :param app_data:
        :return:
        """
        response = 'HTTP/1.1 {status}\r\n'.format(status=self.status)
        for header in self.headers:
            response += '{0}: {1}\r\n'.format(*header)
        response += '\r\n'
        for data in app_data:
            response += data
        return response.encode()

    def serve_forever(self):
        """
        实现监听，处理请求
        :return:
        """
        while True:
            # 接收请求
            self.connection, client_address = self.socket.accept()

            # 发送请求
            self.connection.send(self.handle_request())
            # 关闭连接
            self.connection.close()



if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 8888
    server = WSGIServer((HOST, PORT))
    server.set_application(application)                     # 默认
    # server.set_application(TestMiddle(application))           # 放入中间件
    print('RAPOWSGI Server Serving HTTP service on port {0}'.format(PORT))
    server.serve_forever()