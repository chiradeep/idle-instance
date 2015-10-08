#!/bin/bash

stack_name=$1
stack_user_password=$2

aws cloudformation create-stack --capabilities CAPABILITY_IAM --parameters ParameterKey=IdleInstanceQueueUserPassword,ParameterValue=$stack_user_password --stack-name idleinstancestack0 --template-body file:///$(PWD)/sns_sqs.json

