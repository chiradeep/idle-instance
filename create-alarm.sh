#!/bin/bash


alarm_arn=$1
vm_uuid=$2

alarmname="idleinstance-"$(echo $vm_uuid | awk -F"-"  '{print $1}')


aws cloudwatch put-metric-alarm --alarm-name $alarmname --alarm-description "Alarm when instance is idle for 24 hours" --metric-name CPUUtilization --namespace "CloudStack" --statistic Average --period 3600 --threshold 5 --evaluation-periods 12 --comparison-operator LessThanThreshold --dimensions Name=InstanceUUID,Value=$vm_uuid --alarm-actions $alarm_arn --unit Percent
