# -*- coding: utf-8 -*-
import socket
import threading,time
import re

user =[]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9000))
print "Bind UDP 9000"
while True:
    data, addr = s.recvfrom(1024)
    print data
    data = re.match(r'(\w+):([\w]*)', data.decode('utf-8')).groups()
    if len(data) == 2:
        if data[1] == 'online':
            user.append((data[0], addr))
            for n in user:
                s.sendto(b'%s online...' % data[0].encode('utf-8'), n[1])
            print ('Received from %s:%s' % addr)
            continue
        print ('recevied from %s:%s' % addr)
    for n in user:
        if n[0] != data[0]:
            s.sendto(bytes('>>>' + data[0] + ':' + data[1], encoding='utf-8'), n[1])

