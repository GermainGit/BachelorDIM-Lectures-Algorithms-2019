# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:58:18 2019

@author: prevotge
"""


import argparse
import simple_queue_read as read
import simple_queue_publish as publish

nbOfRead=0


parser = argparse.ArgumentParser()
parser.add_argument("-read",
                    action='store_true')

parser.add_argument("-publish",
                    action='store_true')
args = parser.parse_args()

    
if args.read:
    read.checkMyQueue()
elif args.publish :
    publish.sendMyMessage()
