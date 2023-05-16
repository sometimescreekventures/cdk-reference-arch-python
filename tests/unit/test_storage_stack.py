import aws_cdk as core
import aws_cdk.assertions as assertions

from  networking.networking_stack import NetworkingStack

def test_ec2_created():
    app = core.App()

    stack = NetworkingStack(app, "networkingStackTest")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::EC2::VPC", {
        "EnableDnsHostnames": True,
     })
