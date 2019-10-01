# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:13:10 2019

@author: prevotge
"""

import os
import pika

nbOfRead=1

def callback(ch, method, properties, body):
    global nbOfRead
    print(" [x] Received %r" % body)
    print('Vous avez lu', nbOfRead, 'messages')
    nbOfRead+=1
 

def checkMyQueue():
    
    amqp_url='amqp://qiwsedps:WMXj527zSKlGKFACO2IRj_ZEr4LRU3jg@dove.rmq.cloudamqp.com/qiwsedps'
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    
    channel.queue_declare(queue='presentation')
    
    channel.basic_consume(queue='presentation',
                              on_message_callback=callback,                          
                              auto_ack=True)
        
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()