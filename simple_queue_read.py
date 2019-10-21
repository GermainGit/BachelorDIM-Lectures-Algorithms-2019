# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:13:10 2019

@author: prevotge
"""

import os
import pika
import config

nbOfRead=1

def callback(ch, method, properties, body):
    global nbOfRead
    print(" [x] Received %r" % body)
    print('Vous avez lu', nbOfRead, 'messages')
    nbOfRead+=1
    ch.basic_ack(delivery_tag= method.delivery_tag)

def checkMyQueue():
    
    amqp_url=config.amqp_url
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    
    queue = channel.queue_declare(queue='presentation')
    
    channel.basic_consume(queue='presentation',
                              on_message_callback=callback,                          
                              auto_ack=True)
    print('Vous avez :',queue.method.message_count,' message en file d\'attente')
        
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()