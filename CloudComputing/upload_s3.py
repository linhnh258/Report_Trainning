# Import các thư viện cần thiết
import boto3
import os
import sys
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

AWS_REGION = os.getenv('AWS_REGION')
PROFILE_NAME = os.getenv('AWS_PROFILE_NAME')
BUCKET_NAME = os.getenv('S3_BUCKET_NAME')


local_file_path = sys.argv[1]
s3_object_key = os.path.basename(local_file_path)

try:
    session = boto3.Session(profile_name=PROFILE_NAME)
    s3_client = session.client('s3', region_name=AWS_REGION)

except (NoCredentialsError, PartialCredentialsError) as e:
    print(f"Error, please try '{PROFILE_NAME}'.")
    exit(1)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

try:
    print(f"\nStart upload file ... ")
    print(f"  - From: '{local_file_path}'")
    print(f"  - To bucket: '{BUCKET_NAME}'")
    print(f"  - Object name: '{s3_object_key}'")

    s3_client.upload_file(local_file_path, BUCKET_NAME, s3_object_key)

    print("\nSucessful upload file!")

except FileNotFoundError:
    print(f"Find not found at '{local_file_path}'.")
except ClientError as e:
    # Bắt các lỗi cụ thể từ phía AWS
    if e.response['Error']['Code'] == 'NoSuchBucket':
        print(f"Error: Bucket '{BUCKET_NAME}' invalid")
    else:
        print(f"Error from AWS: {e}")
except Exception as e:
    print(f"Error {e}")

