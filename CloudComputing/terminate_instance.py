# Import các thư viện cần thiết
import boto3
import os
import sys

AWS_REGION = os.getenv('AWS_REGION')
PROFILE_NAME = os.getenv('AWS_PROFILE_NAME')


# Get Instance ID 
instance_id_to_terminate = sys.argv[1]

try:
    session = boto3.Session(profile_name=PROFILE_NAME)
    ec2_client = session.client('ec2', region_name=AWS_REGION)
    print("Sucessful connect")

except Exception as e:
    print(f"Error {e}")
    exit(1)

try:
    ec2_client.terminate_instances(
        InstanceIds=[
            instance_id_to_terminate,
        ]
    )
    
    waiter = ec2_client.get_waiter('instance_terminated')
    waiter.wait(InstanceIds=[instance_id_to_terminate])
    
    print(f"Instance {instance_id_to_terminate} already terminated!")

except Exception as e:
    if 'InvalidInstanceID.NotFound' in str(e):
        print(f" Error: Cannot find instance wwith ID '{instance_id_to_terminate}'.")
    else:
        print(f"Error: {e}")

