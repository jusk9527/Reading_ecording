import socket
if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 8888
    # 初始化
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定
    listen_socket.bind((HOST, PORT))
    # 监听
    listen_socket.listen(1)
    print('Serving HTTP on port %s ...' % PORT)
    while True:
        # 接受请求
        client_connection, client_address = listen_socket.accept()
        # 通信
        request = client_connection.recv(1024)
        print(str(request))
        http_response = 'HTTP/1.1 200 OK\r\n\r\n<html><body>hello</body></html>'
        client_connection.sendall(http_response.encode())
        # 关闭连接
        client_connection.close()
