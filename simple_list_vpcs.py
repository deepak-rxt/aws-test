import boto3

session = boto3.Session(region_name='us-east-1')

ec2_client = session.client('ec2')

# Use the client to describe VPCs
response = ec2_client.describe_vpcs()

for response in response['Vpcs']:
    try:
        for tag in response['Tags']:
            key = tag['Key']
            value = tag['Value']
            if key == 'Name':
                name = value
            print(f"{name}")
    except KeyError:
        pass