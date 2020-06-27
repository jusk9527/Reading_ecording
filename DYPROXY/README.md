### 前言

因为最近发现官方源码挺有趣的，所以引发了在弄一个项目时先分析源码的行为。当我在看 socketserver 源码的时候发现这个标准库确实很漂亮。

那么我们可不可以用一下这个标准库实现下今天的主题呢？自己动手实现一个代理并实现混淆



### 实验分析

1. 我们先得看下有没有简单一点的协议实现**地址封装**

查找资料发现可以使用sock5这个协议，首先通用性非常好。Firefox本身就自带socks这个client端，当然你也可以用其他插件也是可以的。我们只是介绍基础的代理或者说穿透原理，所以基本能简单就都用最简单地方法去实现



这里多说依据sock5协议，sock5协议基于TCP协议上的一种，是通用的代理协议，我们在处理加密传输及其方便，我们还可以吧这个协议转成自己的私有协议。
这是他的官方介绍

https://tools.ietf.org/html/rfc1928


2. 这份协议可以认真看一下，对协议规定的细节非常规范。

其主要是通信双方的规则（最小单位是字节，比如VER 1 表示 1字节，但是值是可以更变的，这需要看详细的协议说明）


```
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

```



### python 语言实践一下





```
class Proxy(Tcp):
    # 用户认证 用户名/密码
    username = 'username'
    password = 'password'

    def handle(self):
        """
        一、客户端认证请求
            +----+----------+----------+
            |VER | NMETHODS | METHODS  |
            +----+----------+----------+
            | 1  |    1     |  1~255   |
            +----+----------+----------+
        """
        # 从客户端读取并解包两个字节的数据
        header = self.connection.recv(2)
        VER, NMETHODS = struct.unpack("!BB", header)
        # 设置socks5协议，METHODS字段的数目大于0
        assert VER == SOCKS_VERSION, 'SOCKS版本错误'
        
        # 接受支持的方法
        # 无需认证：0x00    用户名密码认证：0x02
        # assert NMETHODS > 0
        methods = self.IsAvailable(NMETHODS)
        # 检查是否支持该方式，不支持则断开连接
        if 0 not in set(methods):
            self.server.close_request(self.request)
            return
        
        """
        二、服务端回应认证
            +----+--------+
            |VER | METHOD |
            +----+--------+
            | 1  |   1    |
            +----+--------+
        """
        # 发送协商响应数据包 
        self.connection.sendall(struct.pack("!BB", SOCKS_VERSION, 0))
        
        # 校验用户名和密码
        # if not self.VerifyAuth():
        #    return
        

        """
        三、客户端连接请求(连接目的网络)
            +----+-----+-------+------+----------+----------+
            |VER | CMD |  RSV  | ATYP | DST.ADDR | DST.PORT |
            +----+-----+-------+------+----------+----------+
            | 1  |  1  |   1   |  1   | Variable |    2     |
            +----+-----+-------+------+----------+----------+
        """
        version, cmd, _, address_type = struct.unpack("!BBBB", self.connection.recv(4))
        assert version == SOCKS_VERSION, 'socks版本错误'
        if address_type == 1:       # IPv4
            # 转换IPV4地址字符串（xxx.xxx.xxx.xxx）成为32位打包的二进制格式（长度为4个字节的二进制字符串）
            address = socket.inet_ntoa(self.connection.recv(4))
        elif address_type == 3:     # Domain
            domain_length = ord(self.connection.recv(1)[0])
            address = self.connection.recv(domain_length)
        port = struct.unpack('!H', self.connection.recv(2))[0]

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
        self.connection.sendall(reply)      # 发送回复包

        # 建立连接成功，开始交换数据
        if reply[1] == 0 and cmd == 1:
            self.ExchangeData(self.connection, remote)
        self.server.close_request(self.request)


    def IsAvailable(self, n):
        """ 
        检查是否支持该验证方式 
        """
        methods = []
        for i in range(n):
            methods.append(ord(self.connection.recv(1)))
        return methods


    def VerifyAuth(self):
        """
        校验用户名和密码
        """
        version = ord(self.connection.recv(1))
        assert version == 1
        username_len = ord(self.connection.recv(1))
        username = self.connection.recv(username_len).decode('utf-8')
        password_len = ord(self.connection.recv(1))
        password = self.connection.recv(password_len).decode('utf-8')
        if username == self.username and password == self.password:
            # 验证成功, status = 0
            response = struct.pack("!BB", version, 0)
            self.connection.sendall(response)
            return True
        # 验证失败, status != 0
        response = struct.pack("!BB", version, 0xFF)
        self.connection.sendall(response)
        self.server.close_request(self.request)
        return False


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
                if remote.send(data) <= 0:
                    break
            if remote in rs:
                data = remote.recv(4096)
                if client.send(data) <= 0:
                    break


if __name__ == '__main__':
    # 服务器上创建一个TCP多线程服务，监听2019端口
    Server = ThreadingTCPServer(('0.0.0.0', 2020), Proxy)
    Server.serve_forever();
```

我们先使用firefox 测试下，ok，通过的


我们起个client端看下
如果使用http转socks5协议呢？

```
import requests


url = "https://tools.ietf.org/html/rfc1928"
res = requests.get(url, proxies={"http": "socks5://localhost:2020", "https": "socks5://localhost:2020"})
print(res.status_code)

# 200
```

思考

1. 如果这样的话我们就不能对client端的数据进行加密传输到server端了，那该怎么办呢？我们client端也起一个服务端口，监听一个端口，把监听的端口数据进行加密，然后转发的server端不就可以了吗？



client端监听

```
import select
import socket
import struct
from socketserver import StreamRequestHandler as Tcp, ThreadingTCPServer


class Proxy(Tcp):



    def handle(self):

        self.address = "0.0.0.0"
        self.port = 2020

        self.remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.remote.connect((self.address, self.port))


        bind_address = self.remote.getsockname()

        self.ExchangeData(self.connection, self.remote)

    def ExchangeData(self, client, remote):
        """
        交换数据
        """
        while True:
            # 等待数据
            rs, ws, es = select.select([client, remote], [], [])
            if client in rs:
                data = client.recv(4096)
                if remote.send(data) <= 0:
                    break
            if remote in rs:
                data = remote.recv(4096)
                if client.send(data) <= 0:
                    break

if __name__ == '__main__':
    # 服务器上创建一个TCP多线程服务，监听2019端口
    Server = ThreadingTCPServer(('0.0.0.0', 2019), Proxy)
    Server.serve_forever();
```


这里我们只是单纯在TCP传输中将数据转发。注意这里借用了==firefox==  端以及实现的 SOCKS5。我只是单纯转发。
为什么要这样呢。因为这样方便对数据直接在client端加密解密，也方便在server端加密解密。如果加上现在常见的加密方式会怎么样。我们实践一下


我们先了解一下常见的加密方式

```
MD5         # 通用加密！可以防篡改，理论不可逆，但可以撞彩虹表
DES         # 这个可以暴力破解
3DES        # 升级版DES,可以防止暴力破解
AES         # 对称加密，很多js接口都喜欢用这个小防一下爬虫
SHA         # 很多js接口都喜欢用这个，在数据库存储密码时也和喜欢salt + SHA2做处理
RSA         # 非对称加密，支付宝支付就这个加密
```


加密方式还是非常多的，但是我们只是想单纯混淆下，不必使得算法的时间复杂度那么高，造成CPU去算很多次。

我们可以这样，socket传输的最低单位是字节

1 byte = 8 bit = 00000000-11111111

那么1byte表示的最大值就是255，最小值就是0。
那么这就好办了，取一个256字节的密码。里面包括了0-255这些数字（不重复）。然后使用数组将他们排列，这个时候就有了索引。且传输的时候对单独每个字节加密，到地方的时候解密。对每一个字节进行加密。

我们这个时候算下对单个字节加密的时间复杂度是为O(1)。而组合的结果可以有255*254*253*···=255！种。


那我们的步骤就是
1. 设计一个256字节的密码，包含0-255，且不重复
2. 将密码base64 编码一些。一个是:方便存储，二是:通过base64 在数组与base64编码之间转换
3. 设计一个解码器编辑器，将设计的密码可以很方便的转换为 加密密码器和解密密码器
4. 设计一个传输通道 将我们设计的解码编辑器弄过来，将传输通道中的每个字节加密或解密，然后传输


分成4步走之后我们实际代码实现一下

1. 设计一个256字节的密码，包含0-255，且不重复


```
import random
PASSWORD_LENGTH = 256
IDENTITY_PASSWORD = bytearray(range(256))



# random
def randomPassword():
	password = IDENTITY_PASSWORD.copy()
	random.shuffle(password)
	return password
```


2. 将密码base64 编码 - 解密


```
import base64
# 定义数组长度 256
# len = length
def validatePassword(password):
	return len(password) == PASSWORD_LENGTH and len(set(password)) == PASSWORD_LENGTH


# load
def loadsPassword(passwordString):
	try:
		password = base64.urlsafe_b64decode(passwordString.encode('utf8', errors='strict'))
		password = bytearray(password)
	except:
		raise InvalidPasswordError

	if not validatePassword(password):
		raise InvalidPasswordError

	return password


# dump
def dumpsPassword(password):
	if not validatePassword(password):
		raise InvalidPasswordError

	return base64.urlsafe_b64encode(password).decode('utf8', errors='strict')
```


3. 设计一个解码编辑器


```
import copy


class Cipher():
    def __init__(self, encodePassword, decodePassword):
        # 编码用的密码
        self.encodePassword = encodePassword
        # 解码用的密码
        self.decodePassword = decodePassword

    # 解码加密后的数据到原数据
    def encode(self, bs):
        for i,v in enumerate(bs):
            bs[i] = self.encodePassword[v]



    # 解密加密后的数据到原数据
    def decode(self, bs):
        for i,v in enumerate(bs):
            bs[i] = self.decodePassword[v]


    # 新建一个解密编辑器
    @classmethod
    def NewCipher(cls,encodePassword):
        decodePassword = copy.copy(encodePassword)

        for i,v in enumerate(encodePassword):
            decodePassword[v] = i

        return cls(encodePassword, decodePassword)
```

4. 设计一个传输管道


```
password = "base64 成的密码"


class SecureSocket():


    def __init__(self):
        self.cipher = self._Cipher()

    def _Cipher(self):
        bytepassword = loadsPassword(password)
        cipher = Cipher.NewCipher(bytepassword)
        return cipher

    def decodeRead(self, bs):
        bs = bytearray(bs)
        self.cipher.decode(bs)

        return bs


    def encodeWrite(self, bs):
        bs = bytearray(bs)
        self.cipher.encode(bs)
        return bs
```



我们测试下。ok通过



### go语言实现版本
我们依照上面的步骤，实现一下，ok。通过

1. 这里注意下如果需要使用go 的io.copy方法的话，他其实内部是有一个for 循环，对大的数据比如传输还是非常有帮助的。
2. go的协程还是非常nice的
3. 交叉编译效果也还好！



思考：
1. 我们能否对传输继续加密呢。

是可以的。可以用多种加密对已经加密的数据继续加密，这样相对来说更安全一点

2. 我们能否对已实现的传输进行攻击？

这块就不研究了

3. 可以做什么

千人千面



### 实验总结
1. 实验过程中犯了好几次错误是不该犯的，就是写错了加密的一些标识！
2. socket 编程不好调试。很多时候打断点会出现奇怪的问题，尤其是Goland不知道为什么没有断点调试板
3. 感谢JetBrains提供的Golang、Pycharm 这么优秀的IDE
4. python 现在向后面标准写法看齐，使用typing模块去定义传递类型和返回类型
5. 下一节我们主题是如何使用异步造一个websocket框架进行直播流的解析

参考资料：

https://jiajunhuang.com/articles/2019_06_06-socks5.md.html

https://tools.ietf.org/html/rfc1928



