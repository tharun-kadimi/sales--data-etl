import boto3
from openpyxl import load_workbook
import boto3,os
import pandas as pd 
from io import BytesIO
from datetime import datetime, timezone

s3_client= boto3.client('s3')
s3= boto3.resource('s3')

bucket_name = 'sales--data-etl'

objectdf1= s3_client.get_object(Bucket=bucket_name,Key='sales_data.csv') 
SalesDf=pd.read_csv(objectdf1['Body'])
print(SalesDf) 
response = s3_client.head_object(Bucket=bucket_name, Key='sales_data.csv')
last_modified = response['LastModified']

# Get today's date in UTC (same timezone as the file's LastModified)
today = datetime.now(timezone.utc)

# Check if the file was uploaded today
if last_modified.date() == today.date():
    print(f"The file 'sales_data.csv' was uploaded today ({last_modified.date()}).")
else:
    print(f"The file 'sales_data.csv' was uploaded on {last_modified.date()}, not today.")


objectdf2= s3_client.get_object(Bucket=bucket_name,Key='customer_data.json') 
CustomerDf=pd.read_json(objectdf2['Body'])
# print(CustomerDf) 

objectdf3= s3_client.get_object(Bucket=bucket_name,Key='product_data.xlsx') 
ProductDf=pd.read_excel(BytesIO(objectdf3['Body'].read()))
# print(ProductDf) 
