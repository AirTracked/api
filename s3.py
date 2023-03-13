import logging
import boto3
from botocore.exceptions import ClientError
from fastapi import File, UploadFile
import os

AWS_REGION = "eu-central-1"
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_BUCKET = "airtrack-test"

def upload_file_to_s3(file: UploadFile):
    s3 = boto3.client('s3', region_name=AWS_REGION,
                      aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    file_content = file.file.read()
    s3.put_object(Bucket=AWS_BUCKET, Key=file.filename, Body=file_content)