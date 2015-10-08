#!/usr/bin/python

import boto3
import psutil
import sys
import time

def send_cpu(vm_name, vm_uuid):
    client = boto3.client('cloudwatch')
    while True:
        response = client.put_metric_data(
             Namespace='cloudstack',
             MetricData=[
                 {
                     'MetricName' : 'cpu',
                     'Dimensions' : [
                         {
                             'Name' : 'InstanceUUID',
                             'Value': vm_uuid
                         },
                         {
                             'Name' : 'InstanceName',
                             'Value': vm_name
                         },
                     ],
                     'Value': psutil.cpu_percent(),
                     'Unit' : 'Percent',
                 },
            ]     
         )
        print("Sent cpu %s" % psutil.cpu_percent())
        time.sleep(60)
    
def main(argv):
   vm_name = argv[0]
   vm_uuid = argv[1]

   #print("VM Name is %s and uuid is %s" % (vm_name,vm_uuid))
   send_cpu(vm_name, vm_uuid)

if __name__ == '__main__':
    #NOTE: vm name and uuid can be obtained from 
    #http://<dhcp server address>/latest/local-hostname and 
    #http://<dhcp server address>/latest/instance-id
   main(sys.argv[1:])
