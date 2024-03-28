import boto3

session = boto3.Session(region_name='us-east-1')
account_ids = ['account_id1', 'account_id2', 'account_id3', 'account_id4', 'account_id5']
for account_id in account_ids:
    # Create a session using STS Assume Role
    sts_client = boto3.client('sts')
    assumed_role = sts_client.assume_role(
        RoleArn=f'arn:aws:iam::{account_id}:role/your-role-name',
        RoleSessionName='AssumedRoleSession'
    )
    credentials = assumed_role['Credentials']

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