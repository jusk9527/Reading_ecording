
import select
import socket
from socketserver import StreamRequestHandler as Tcp, ThreadingTCPServer
from DYPROXY.module.securesocket import SecureSocket


class Proxy(Tcp):


    def handle(self):

        self.address = "0.0.0.0"
        self.port = 2020

        print("客户端：", self.client_address, " 请求连接！")

        self.remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.remote.connect((self.address, self.port))


        print('已建立连接：', self.address, self.port)
        # print(self.connection)
        self.ExchangeData(self.connection, self.remote)



    def ExchangeData(self, client, remote):
        """
        交换数据
        """
        securesocket = SecureSocket()

        while True:
            # 等待数据
            rs, ws, es = select.select([client, remote], [], [])
            if client in rs:
                data = client.recv(4096)

                # 加密
                _data =securesocket.encodeWrite(data)
                if remote.send(_data) <= 0:
                    break
            if remote in rs:
                data = remote.recv(4096)
                # 解密
                _data = securesocket.decodeRead(data)
                if client.send(_data) <= 0:
                    break

if __name__ == '__main__':
    # 服务器上创建一个TCP多线程服务，监听2019端口
    Server = ThreadingTCPServer(('0.0.0.0', 2019), Proxy)
    print("**********************************************************")
    print("************************* DYPROXY ************************")
    print("*************************   1.0   ************************")
    print("********************  IP:xxx.xxx.xx.xx  ******************")
    print("***********************  PORT:2019  **********************")
    print("**********************************************************")
    Server.serve_forever()