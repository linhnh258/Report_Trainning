import boto3
import os

AMI_ID = os.getenv('AWS_AMI_ID')
INSTANCE_TYPE = os.getenv('AWS_INSTANCE_TYPE', 't2.nano') 
KEY_NAME = os.getenv('AWS_KEY_NAME')
SECURITY_GROUP_ID = os.getenv('AWS_SECURITY_GROUP_ID')
SUBNET_ID = os.getenv('AWS_SUBNET_ID')
AWS_REGION = os.getenv('AWS_REGION')
PROFILE_NAME = os.getenv('AWS_PROFILE_NAME')

try:
    session = boto3.Session(profile_name=PROFILE_NAME)
    ec2_client = session.client('ec2', region_name=AWS_REGION)

except Exception as e:
    print(f"Cannot Swtich role - Error: {e}")
    ec2_client = boto3.client('ec2', region_name=AWS_REGION)


try:
    response = ec2_client.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        MinCount=1,
        MaxCount=1,
        NetworkInterfaces=[
            {
                'DeviceIndex': 0,
                'Groups': [SECURITY_GROUP_ID],
                'AssociatePublicIpAddress': True
            }
        ],
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'VolumeSize': 10,
                    'VolumeType': 'gp3',
                    'DeleteOnTermination': True
                },
            },
        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'My-Boto3-Server'
                    },
                ]
            },
        ]
    )

    instance_id = response['Instances'][0]['InstanceId']
    waiter = ec2_client.get_waiter('instance_running')

    waiter.wait(InstanceIds=[instance_id])
    
    instance_info = ec2_client.describe_instances(InstanceIds=[instance_id])
    public_ip = instance_info['Reservations'][0]['Instances'][0].get('PublicIpAddress', 'N/A')
    private_ip = instance_info['Reservations'][0]['Instances'][0].get('PrivateIpAddress', 'N/A')
    instance_type = instance_info['Reservations'][0]['Instances'][0].get('InstanceType', 'N/A')

    print(f"Instance ready!")
    print(f"   - ID: {instance_id}")
    print(f"   - Type: {instance_type}")
    print(f"   - Public IP Address: {public_ip}")
    print(f"   - Private IP Address: {private_ip}")

except Exception as e:
    print(f"Error: {e}")

