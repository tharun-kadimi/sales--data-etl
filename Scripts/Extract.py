import boto3
from openpyxl import load_workbook
import boto3,os
import pandas as pd 
from io import BytesIO
from datetime import datetime, timezone

s3_client= boto3.client('s3')
s3= boto3.resource('s3')

def common_extraction(bucket_name,file_name):
    file_extension=file_name.split('.')[-1]
    if file_extension=='csv':
        objectdf= s3_client.get_object(Bucket=bucket_name,Key=file_name) 
        Df=pd.read_csv(objectdf['Body'])
    elif file_extension=='json':
        objectdf= s3_client.get_object(Bucket=bucket_name,Key=file_name) 
        Df=pd.read_json(objectdf['Body'])
    elif file_extension=='xlsx':
        objectdf= s3_client.get_object(Bucket=bucket_name,Key=file_name) 
        Df=pd.read_excel(BytesIO(objectdf['Body'].read()))
    print(Df) 
    response= s3_client.head_object(Bucket=bucket_name, Key=file_name)
    last_modified= response['LastModified']

    # Get today's date in UTC (same timezone as the file's LastModified)
    today = datetime.now(timezone.utc)

    # Check if the file was uploaded today
    if last_modified.date() == today.date():
        print(f"The file {file_name} was uploaded today ({last_modified.date()}).")
        return Df
    else:
        print(f"The file {file_name} was uploaded on {last_modified.date()}, not today.")
        
