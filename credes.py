s3=$(aws s3api list-buckets --query "Buckets[?Name=='athena-access-test-bucket-april-2'].Name" --output json)
s3_count=$(echo "$s3" | jq 'if type == "array" then length else 0 end')
echo "$s3_count"

ec2_client = boto3.client('ec2',
                              aws_access_key_id=credentials['AccessKeyId'],
                              aws_secret_access_key=credentials['SecretAccessKey'],
                              aws_session_token=credentials['SessionToken'],
                              region_name='your_region')
