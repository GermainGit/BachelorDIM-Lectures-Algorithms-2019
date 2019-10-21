# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:58:18 2019

@author: prevotge
"""


import argparse
import simple_queue_read as read
import simple_queue_publish as publish


parser = argparse.ArgumentParser()
parser.add_argument("-read",
                    action='store_true')

parser.add_argument("-publish",
                    action='store_true')

parser.add_argument("-concurency",
                    action='store_true')

args = parser.parse_args()


# =============================================================================
# When you call this script, you can add an argument to call different function : Publish or Read mode
# Example : $ python queue_publish_read.py -read
# =============================================================================

    
if args.read:
    read.checkMyQueue()
elif args.publish :
    publish.publish(False)
elif args.concurency:
    publish.publish(True)    
