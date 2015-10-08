#!/bin/bash

stack_name=$1
aws cloudformation describe-stacks --stack-name $stack_name | grep Output 
