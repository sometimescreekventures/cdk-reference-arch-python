from aws_cdk import  Stack
from aws_cdk.aws_ec2 import Vpc, SubnetConfiguration, SubnetType
from constructs import Construct

class NetworkingStack(Stack):

    vpc = None

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        myVpc = Vpc(self, "stackVpc",
                    subnet_configuration=[
                SubnetConfiguration(
                    name = 'Public-Subent',
                    subnet_type = SubnetType.PUBLIC,
                    cidr_mask = 26
                ),
                SubnetConfiguration(
                    name = 'Private-Subnet',
                    subnet_type = SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask = 26
                )
            ],)
        self.vpc = myVpc
