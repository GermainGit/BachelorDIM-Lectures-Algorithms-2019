# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:09:50 2019

@author: prevotge

"""


import os
import pika
import config

def connectMe():
    amqp_url=config.amqp_url
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    
    channel.queue_declare(queue='coucou')
    
    return channel, connection

def sendMyMessage(channel, connection):
    

    
    channel.basic_publish(exchange='',
                              routing_key='coucou',
                              body='Hello World !')
                              
    print(" [x] Sent 'Hello World!'")
        
    connection.close()
    
    
def sendMyMessageConcurency(channel, connection):
        
    channel.basic_publish(exchange='',
                              routing_key='coucou',
                              body='Hello World !',
                              properties=pika.BasicProperties(
                                      delivery_mode = 2))
                              
    print(" [x] Sent 'Hello World! ")
        
    connection.close()
    
def publish(concurrency):
    channel, connection = connectMe()
    if concurrency :
        sendMyMessageConcurency(channel, connection)
    else:
        sendMyMessage(channel, connection)
        
    
    