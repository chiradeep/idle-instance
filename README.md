# idle-instance
Terminate idle instances on cloudstack using AWS
![Image of Alarm Architecture](https://github.com/chiradeep/idle-instance/blob/master/cloudstack_collab_oct_2015_sns.jpg)

##Pre-requisites
1. CloudStack cloud
2. AWS CLI and AWS account API keys
3. cloudmonkey (pip install cloudmonkey) and boto3 (pip install boto3) on the MS
4. boto3, psutil on each cloudstack instance

##Usage
1. Create Alarm Topic in SNS, SQS and API keys for Queue/SNS user
```bash
$ ./create-sqs-sns.sh <stack-name> <password for new IAM user to create>
E.g.,
$ ./create-sqs-sns.sh idleinstancestack l@mep@assword
```
2. Grab the outputs of the stack after it is created
```bash
$ ./outputs.sh idleinstancestack
"OutputKey": "IdleInstanceAlarmSNSTopicTopicARN", 
   "OutputValue": "arn:aws:sns:us-west-2:987605588178:idleinstancestack0-IdleInstanceAlarmSNSTopic-BKKKKKKKKKKK"
"OutputKey": "IdleInstanceQueueInfo", 
   "OutputValue": "ARN: arn:aws:sqs:us-west-2:388888888888:idleinstancestack0-IdleInstanceQueue-KJJJJJJJJ URL: https://sqs.us-west-2.amazonaws.com/333333333333/idleinstancestack0-IdleInstanceQueue-KKKKKKKKKK"
"OutputKey": "IdleInstanceQueueUserInfo", 
   "OutputValue": "ARN: arn:aws:iam::384845588177:user/idleinstancestack0-IdleInstanceQueueUser-1FBJ8C0SOTGPR Access Key: AKIAABCDEDFHJKCIQNAD Secret Key: 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"
```
3. Every time a VM is created, grab its UUID (say off of the event queue) and create an idle instance alarm.
```bash
$ ./create-alarm.sh <IdleInstanceAlarmSNSTopicTopicARN from output> <vm uuid>
```
4. Inside each VM use the cpu.py script to sent CloudWatch metrics (customize the AWS region) every few minutes
5. On the MS, run a job with sqs.py to fetch and delete the idle VM uuids.

