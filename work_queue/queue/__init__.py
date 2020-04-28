#!/usr/bin/env python
# encoding: utf-8
'''
@Author: winston he
@Email: winston.wz.he@gmail.com
@File: __init__.py.py
@Time: 2020/4/26 16:24
'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

'''
in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one. 
Instead, it will dispatch it to the next worker that is not still busy.
'''
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='hello', durable=False) # create a queue
channel.queue_declare(queue='hi', durable=True) # create a queue, this queue will survive even it experiences a server shutdown.
