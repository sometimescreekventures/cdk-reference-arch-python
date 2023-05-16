### Create Reference Architecture as part of Dev/Ops interview


## The reference Architecture consist of:
 - 1 s3 bucket 
 - 1 vpc
    - 1 subnet
        - 2 ec2
        - 2 EBS one connected to each ec2

## Requirements
# Stacks
    3 different stacks to be used
    - Networking
    - Compute and storage
    - s3
# Language
Python

Stragety 
Create each stack as its own module that can be called with other stacks
Allow multiple envirornments
add testing if time 
2 hours
