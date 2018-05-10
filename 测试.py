# -*- coding: UTF-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80))

s.send('POST / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
Buff = []
while True:
    d = s.recv(1024)
    if d:
        Buff.append(d)
    else:
        break
data = ''.join(Buff)
s.close()

a = data.split('\r\n\r\n')
print a[0]
