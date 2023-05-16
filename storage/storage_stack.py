from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from aws_cdk.aws_ec2 import Instance, InstanceType, SubnetSelection, SubnetType, MachineImage, InstanceType, InstanceClass, InstanceSize
from constructs import Construct



class StorageStack(Stack):


    def create_ec2_with_ebs(self, id: str, vpc_id ) -> Construct:
        host = Instance(self, id,
                            instance_type=InstanceType.of(InstanceClass.BURSTABLE2, InstanceSize.MICRO),
                            instance_name="mySingleHost",
                            machine_image=MachineImage.latest_amazon_linux2023(),
                            vpc=vpc_id,
                            vpc_subnets=SubnetSelection(
                            subnet_type=SubnetType.PRIVATE_WITH_EGRESS),
                            )
        # ec2.Instance has no property of BlockDeviceMappings, add via lower layer cdk api:
        host.instance.add_property_override("BlockDeviceMappings", [{
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "VolumeSize": "10",
                "VolumeType": "io1",
                "Iops": "150",
                "DeleteOnTermination": "true"
            }
        }, {
            "DeviceName": "/dev/sdb",
            "Ebs": {"VolumeSize": "30"}
        }
        ])
        return host 


    def __init__(self, scope: Construct, construct_id: str, NetworkingStack, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.create_ec2_with_ebs("ec2_first", NetworkingStack.vpc)
        self.create_ec2_with_ebs( "ec2_second", NetworkingStack.vpc)


        