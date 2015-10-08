#!/usr/bin/python

import boto3
import json
import time

#QUEUE = 'https://sqs.us-west-2.amazonaws.com/384845588177/cloudstack-unused-instances'
QUEUE = 'cloudstack-unused-instances'


sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName=QUEUE)

while True:
   for message in queue.receive_messages():
      m = json.loads(message.body) 
      m1 = json.loads(m['Message'].replace("'", "\""))
      dimensions = m1['Trigger']['Dimensions']
      instance_details = {d['name']:d['value'] for d in dimensions}
      for k,v in instance_details.iteritems(): 
         print "Key= %s , Value=%s" % (k,v)
      message.delete()
   time.sleep(60)
