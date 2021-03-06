import socket
import multiprocessing
import re


class WSGIServer(object):

    def __init__(self):
        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.tcp_server_socket.bind(("", 7890))
        # 变为监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        """
        为客户端返回数据
        :return:
        """
        # 接受浏览器发送过来的请求，即http请求
        request = new_socket.recv(1024).decode('utf-8')
        print(request)
        # 返回http格式的数据
        response_body = open("www_egiraffe_com_default.html", 'r', encoding='utf-8').read()
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "\r\n"
        response = response_header + response_body
        new_socket.send(response.encode("UTF-8"))

        new_socket.close()

    def run_forever(self):
        # 为这个客户端服务
        while True:
            # 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            # service_client(new_socket)
            p.start()
            new_socket.close()
        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个web服务器对象，然后调用这个对象的run_forever方法运行"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
