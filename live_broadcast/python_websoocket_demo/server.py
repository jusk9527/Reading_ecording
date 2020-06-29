import asyncio
import base64
from hashlib import sha1
import logging

logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', level=logging.DEBUG)


def parse_headers(headers: str) -> dict:
    """
    解析 headers

    :param headers_str: headers 字符串
    :return: headers 字典
    """

    return dict(header.split(': ') for header in headers.split('\r\n')[1:-2])


def generate_key(key: str) -> str:
    """
    握手时，服务端生成 Sec-WebSocket-Accept

    :param key: Sec-WebSocket-Key
    :return: 生成的 Sec-WebSocket-Accept 字符串
    """

    s = f'{key}258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    m = sha1()
    m.update(s.encode('utf-8'))
    return base64.standard_b64encode(m.digest()).decode('utf-8')


class EchoServerProtocol(asyncio.Protocol):
    CONNECTING = 0
    OPEN = 1

    def __init__(self):
        self.transport = None
        self.state = self.CONNECTING
        self.peername = None

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        logging.info(f'客户端 {self.peername} 已连接')
        self.transport = transport

    def data_received(self, data):
        if self.state == self.CONNECTING:  # 握手阶段
            client_headers = parse_headers(data.decode('utf-8'))
            key = client_headers.get('Sec-WebSocket-Key')

            if not key:
                logging.error('客户端的 headers 必须包含 Sec-WebSocket-Key')
                self.transport.close()
                return

            server_headers = [
                'HTTP/1.1 101 Switching Protocols',
                'Upgrade: websocket',
                'Connection: Upgrade',
                f'Sec-WebSocket-Accept: {generate_key(key)}'
            ]
            server_headers = '\r\n'.join(server_headers) + '\r\n' * 2
            self.transport.write(server_headers.encode('utf-8'))
            self.state = self.OPEN
            logging.debug('握手完成')
        elif self.state == self.OPEN:  # 数据传送阶段
            # 读取第一个字节
            first_byte = data[0]
            fin = (first_byte & 0x80) >> 7
            opcode = first_byte & 0x0f

            if opcode == 0x08:
                logging.info(f'客户端 {self.peername} 断开连接')
                self.transport.close()
                return
            if opcode != 0x01:
                msg = '不支持非文本类型'
                logging.info(msg)
                self.send_data(msg)
                self.transport.close()
                return

            # 读取第二个字节
            second_byte = data[1]
            mask = (second_byte & 0x80) >> 7
            if mask == 0x00:
                msg = '客户端必须对 payload data 进行 mask'
                logging.info(msg)
                self.send_data(msg)
                self.transport.close()
                return

            payload_len = second_byte & 0x7f
            if payload_len == 0x7e:
                msg = '不支持长度为 126 的 payload data'
                logging.info(msg)
                self.send_data(msg)
                self.transport.close()
                return
            if payload_len == 0x7f:
                msg = '不支持长度为 127 的 payload data'
                logging.info(msg)
                self.send_data(msg)
                self.transport.close()
                return

            mask_key = data[2:6]
            app_data = data[6:]
            decoded = self.decode(mask_key, app_data).decode("utf-8")
            logging.info(f'客户端 {self.peername} 发来：{decoded}')
            self.send_data(decoded)

    def decode(self, mask_key: bytes, data: bytes):
        return b"".join(bytes((byte ^ mask_key[i % 4],)) for i, byte in enumerate(data))

    def send_data(self, data: str):
        """
        FIN = 1  最后一帧，1 bit
        rsv1 - rsv3 = 000   保留值，3 bits
        opcode = 0001  文本类型，4 bits
        上面组合得到：0x81 = 0b10000001

        mask = 0  服务端不用掩码，1 bit
        payload_len  payload 的长度，7 bits
        上面直接用 bytes((payload_len,)) 可以得到

        payload data  剩余全是 payload data，包含 extension data 和 application data，前者这里不考虑

        :param data: 要发送的文本
        :return:
        """

        msg = f"服务端：{data}".encode('utf-8')
        send_data = bytes((0x81, len(msg))) + msg
        self.transport.write(send_data)



async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(),
        '127.0.0.1', 8080)

    async with server:
        logging.info(f'服务器运行在 {server.sockets[0].getsockname()}')
        await server.wait_closed()


asyncio.run(main())