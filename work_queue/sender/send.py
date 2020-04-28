#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: send.py
@Time: 2020/4/26 16:22
'''
import sys
from simple_queue.queue import channel, connection

msg = ''.join(sys.argv[1:]) or "Hello World...."

channel.basic_publish(exchange='', routing_key='hello', body=msg)
print(" [x] Sent %r" % msg)
connection.close()