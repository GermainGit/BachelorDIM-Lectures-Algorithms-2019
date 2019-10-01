# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:49:12 2019

@author: prevotge
"""

import os
import pika

mode='_SEND'

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
amqp_url='amqp://qiwsedps:WMXj527zSKlGKFACO2IRj_ZEr4LRU3jg@dove.rmq.cloudamqp.com/qiwsedps'

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='hello')


if mode == 'SEND':
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
                          
    print(" [x] Sent 'Hello World!'")
    
    connection.close()
else:
        
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
