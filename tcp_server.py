#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'

import socket, sys

class InfoServer:
    def __init__(self, port):
        self.host = 'localhost'
        self.my_buffer = 2048     # buffer
        self.backlog = 5
        self.client = None
        self.port = port

    def server(self, port):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_address = self.host, port

        print 'starting server at %s:%s' % server_address

        sock.bind(server_address)
        sock.listen(self.backlog)
        while True:
            self.client, address = sock.accept()     # wait forever for an incoming connection
            data = self.client.recv(self.my_buffer)
            self.client.close()

    def send(self, msg):
        self.client.send('done')

if __name__ == '__main__':
    InfoServer(8088)

