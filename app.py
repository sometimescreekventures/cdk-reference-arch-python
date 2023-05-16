#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3.s3_stack import S3Stack
from networking.networking_stack import NetworkingStack
from storage.storage_stack import StorageStack

app = cdk.App()

dev_env=cdk.Environment(account='99999', region='us-east-1')

networking_stack = NetworkingStack(app, "DevNetworking", env=dev_env)

S3Stack(app, "DevS3", env=dev_env)

StorageStack(app, "DevStorage", env=dev_env, NetworkingStack=networking_stack)



app.synth()
