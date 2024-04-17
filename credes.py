aws s3api list-buckets --query "Buckets[?starts_with(Tags[?Key=='Name'] | [0].Value, '$tag_value')].Name" --output text

ec2_client = boto3.client('ec2',
                              aws_access_key_id=credentials['AccessKeyId'],
                              aws_secret_access_key=credentials['SecretAccessKey'],
                              aws_session_token=credentials['SessionToken'],
                              region_name='your_region')
