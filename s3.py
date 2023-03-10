import logging
import boto3
from botocore.exceptions import ClientError
from fastapi import File, UploadFile
import os

AWS_REGION = "eu-central-1"
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

def upload_file(bucket, object_name=None,file: UploadFile = File(...)):
    """Upload a file to an S3 bucket

    :param file: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file)

    # Login to AWS S3
    s3_client = boto3.client('s3',region_name = AWS_REGION,
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

    # Upload the file
    try:
        print(file)
        print(file)
        print(bucket)
        print(object_name)
        #response = s3_client.upload_file(file, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True