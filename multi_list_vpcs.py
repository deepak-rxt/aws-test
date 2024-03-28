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
        name = 'NA'
        application = 'NA'
        created_by = 'NA'
        creation_date = 'NA'
        env = 'NA'
        description = 'NA'
        try:
            for tag in response['Tags']:
                key = tag['Key']
                value = tag['Value']
                if key == 'Name':
                    name = value
                elif key == 'Application':
                    application = value
                elif key == 'CreatedBy':
                    created_by = value
                elif key == 'CreationDate':
                    creation_date = value
                elif key == 'Environment':
                    env = value
                elif key == 'Description':
                    description = value
            print(f"{name},{application},{env},{created_by},{creation_date},{description}")
        except KeyError:
            pass
        
