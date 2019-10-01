# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:09:50 2019

@author: prevotge
"""


import os
import pika

def sendMyMessage():

    amqp_url='amqp://qiwsedps:WMXj527zSKlGKFACO2IRj_ZEr4LRU3jg@dove.rmq.cloudamqp.com/qiwsedps'
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    
    channel.queue_declare(queue='presentation')
    
    channel.basic_publish(exchange='',
                              routing_key='presentation',
                              body='Hello World !')
                              
    print(" [x] Sent 'Hello World!'")
        
    connection.close()