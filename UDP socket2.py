# -*- coding: utf-8 -*-
import socket
import threading, re
import time


def udplink(sock, addr):
    while True:
        time.sleep(0.1)
        print (sock.recv(1024).decode('utf-8'))


print ('input your server ip:')

while True:
    ip = raw_input()
    if re.match(r'\d{3}.\d{1}.\d{1}.\d{1}', ip):
        break
    print ('unlawfun IP')
name = raw_input('input your name :')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.sendto(bytes(name + ':' + 'online', enconding='utf-8'), (ip, 9000))
s.sendto(bytes(name + ':'+'online'), (ip, 9000))
t = threading.Thread(target=udplink, args=(s, (ip, 9000)))
t.start()
while True:
    data = raw_input()
    s.sendto(bytes(name + ':' + data), (ip, 9000))
s.close()
