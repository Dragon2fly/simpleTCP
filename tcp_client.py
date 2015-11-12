#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'

import socket, sys

host = 'localhost'
my_buffer = 2048     # buffer

def client(port, me):
    sock = socket.socket()
    server_address = host, port

    print 'connect to %s:%s' % server_address

    sock.connect(server_address)

    try:
        message = 'I want to tell you that ' + me
        sock.sendall(message)
        data = sock.recv(my_buffer)
        print 'Server said '+data

    except socket.errno, e:
        print 'Socket error: ' + str(e)
    except Exception, e:
        print 'program error: '+ str(e)
    finally:
        print 'close connection'
        sock.close()

if __name__ == '__main__':
    while True:
        msg = raw_input('what to send to server?: ')
        if not msg:
            break

        client(8088, msg)