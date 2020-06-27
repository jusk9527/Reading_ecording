# -*- coding: utf-8 -*-

import select
import socket
import struct
from socketserver import StreamRequestHandler as Tcp, ThreadingTCPServer

SOCKS_VERSION = 5                           # socks版本

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    一、客户端认证请求
        +----+----------+----------+
        |VER | NMETHODS | METHODS  |
        +----+----------+----------+
        | 1  |    1     |  1~255   |
        +----+----------+----------+
    二、服务端回应认证
        +----+--------+
        |VER | METHOD |
        +----+--------+
        | 1  |   1    |
        +----+--------+
    三、客户端连接请求(连接目的网络)
        +----+-----+-------+------+----------+----------+
        |VER | CMD |  RSV  | ATYP | DST.ADDR | DST.PORT |
        +----+-----+-------+------+----------+----------+
        | 1  |  1  |   1   |  1   | Variable |    2     |
        +----+-----+-------+------+----------+----------+
    四、服务端回应连接
        +----+-----+-------+------+----------+----------+
        |VER | REP |  RSV  | ATYP | BND.ADDR | BND.PORT |
        +----+-----+-------+------+----------+----------+
        | 1  |  1  |   1   |  1   | Variable |    2     |
        +----+-----+-------+------+----------+----------+

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""



from DYPROXY.module.securesocket import SecureSocket

class Proxy(Tcp):

    def handle(self):
        self.securesocket = SecureSocket()

        """
        一、客户端认证请求
            +----+----------+----------+
            |VER | NMETHODS | METHODS  |
            +----+----------+----------+
            | 1  |    1     |  1~255   |
            +----+----------+----------+
        """
        # 从客户端读取并解包两个字节的数据

        header = self.connection.recv(3)



        header = self.securesocket.decodeRead(header)
        # 这里是解包
        VER, NMETHODS, _ = struct.unpack("!BBB", header)
        # 设置socks5协议，METHODS字段的数目大于0
        assert VER == SOCKS_VERSION, 'SOCKS版本错误'

        
        """
        二、服务端回应认证
            +----+--------+
            |VER | METHOD |
            +----+--------+
            | 1  |   1    |
            +----+--------+
        """
        # 发送协商响应数据包

        # 发送协商响应数据包，不需要验证，直接通过
        reply = self.securesocket.encodeWrite([SOCKS_VERSION,0])

        self.connection.sendall(struct.pack("!BB", reply[0], reply[1]))



        """
        三、客户端连接请求(连接目的网络)
            +----+-----+-------+------+----------+----------+
            |VER | CMD |  RSV  | ATYP | DST.ADDR | DST.PORT |
            +----+-----+-------+------+----------+----------+
            | 1  |  1  |   1   |  1   | Variable |    2     |
            +----+-----+-------+------+----------+----------+
        """


        res = self.connection.recv(4)

        deres = self.securesocket.decodeRead(res)


        version, cmd, _, address_type = struct.unpack("!BBBB", deres)



        assert version == SOCKS_VERSION, 'socks版本错误'
        if address_type == 1:       # IPv4
            # 转换IPV4地址字符串（xxx.xxx.xxx.xxx）成为32位打包的二进制格式（长度为4个字节的二进制字符串）

            _address = self.connection.recv(4)
            _address = self.securesocket.decodeRead(_address)
            address = socket.inet_ntoa(_address)
        elif address_type == 3:     # Domain

            _domain_length = self.connection.recv(1)
            _domain_length = self.securesocket.decodeRead(_domain_length)[0]
            domain_length = ord(_domain_length)
            address = self.connection.recv(domain_length)

        _port = self.connection.recv(2)
        _port = self.securesocket.decodeRead(_port)
        port = struct.unpack('!H', _port)[0]


        """
        四、服务端回应连接
            +----+-----+-------+------+----------+----------+
            |VER | REP |  RSV  | ATYP | BND.ADDR | BND.PORT |
            +----+-----+-------+------+----------+----------+
            | 1  |  1  |   1   |  1   | Variable |    2     |
            +----+-----+-------+------+----------+----------+
        """
        # 响应，只支持CONNECT请求
        try:
            if cmd == 1:  # CONNECT
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
                print('已建立连接：', address, port)
            else:
                self.server.close_request(self.request)
            addr = struct.unpack("!I", socket.inet_aton(bind_address[0]))[0]
            port = bind_address[1]
            reply = struct.pack("!BBBBIH", SOCKS_VERSION, 0, 0, address_type, addr, port)
        except Exception as err:
            print(err)
            # 响应拒绝连接的错误
            reply = self.ReplyFaild(address_type, 5)


        reply = self.securesocket.encodeWrite(reply)
        self.connection.sendall(reply)      # 发送回复包


        reply = self.securesocket.decodeRead(reply)



        # 建立连接成功，开始交换数据
        if reply[1] == 0 and cmd == 1:
            self.ExchangeData(self.connection, remote)
        self.server.close_request(self.request)





    def ReplyFaild(self, address_type, error_number):
        """ 
        生成连接失败的回复包 
        """
        return struct.pack("!BBBBIH", SOCKS_VERSION, error_number, 0, address_type, 0, 0)


    def ExchangeData(self, client, remote):
        """ 
        交换数据 
        """


        while True:
            # 等待数据
            rs, ws, es = select.select([client, remote], [], [])
            if client in rs:
                data = client.recv(4096)

                # 解密
                _data = self.securesocket.decodeRead(data)
                if remote.send(_data) <= 0:
                    break
            if remote in rs:
                data = remote.recv(4096)
                # 加密
                _data = self.securesocket.encodeWrite(data)

                if client.send(_data) <= 0:
                    break


if __name__ == '__main__':
    # 服务器上创建一个TCP多线程服务，监听2019端口
    Server = ThreadingTCPServer(('0.0.0.0', 2020), Proxy)
    print("**********************************************************")
    print("************************* DYPROXY ************************")
    print("*************************   1.0   ************************")
    print("********************  IP:xxx.xxx.xx.xx  ******************")
    print("***********************  PORT:2020  **********************")
    print("**********************************************************")
    Server.serve_forever()
