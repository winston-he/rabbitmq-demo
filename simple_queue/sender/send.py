#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: send.py
@Time: 2020/4/26 16:22
'''
from simple_queue.queue import channel, connection

channel.basic_publish(exchange='', routing_key='hello', body="this is amazing")
connection.close()