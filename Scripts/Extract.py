import boto3
from openpyxl import load_workbook
import boto3,os
import pandas as pd 
from io import BytesIO
from datetime import datetime, timezone

s3_client= boto3.client('s3')
s3= boto3.resource('s3')

bucket_name = 'sales--data-etl'
sales_data='sales_data.csv'
customer_data='customer_data.json'
product_data='product_data.xlsx'

objectdf1= s3_client.get_object(Bucket=bucket_name,Key=sales_data) 
SalesDf=pd.read_csv(objectdf1['Body'])
print(SalesDf) 
response1 = s3_client.head_object(Bucket=bucket_name, Key=sales_data)
last_modified_f1 = response1['LastModified']

# Get today's date in UTC (same timezone as the file's LastModified)
today = datetime.now(timezone.utc)

# Check if the file was uploaded today
if last_modified_f1.date() == today.date():
    print(f"The file {sales_data} was uploaded today ({last_modified_f1.date()}).")
else:
    print(f"The file {sales_data} was uploaded on {last_modified_f1.date()}, not today.")


#customer_data_section
objectdf2= s3_client.get_object(Bucket=bucket_name,Key=customer_data) 
CustomerDf=pd.read_json(objectdf2['Body'])
print(CustomerDf) 
response2 = s3_client.head_object(Bucket=bucket_name, Key=customer_data)
last_modified_f2 = response2['LastModified']

today = datetime.now(timezone.utc)

if last_modified_f2.date() == today.date():
    print(f"The file {customer_data} was uploaded today ({last_modified_f2.date()}).")
else:
    print(f"The file {customer_data} was uploaded on {last_modified_f2.date()}, not today.")


#product_data_section
objectdf3= s3_client.get_object(Bucket=bucket_name,Key=product_data) 
ProductDf=pd.read_excel(BytesIO(objectdf3['Body'].read()))
print(ProductDf) 
response3 = s3_client.head_object(Bucket=bucket_name, Key=product_data)
last_modified_f3 = response3['LastModified']

today = datetime.now(timezone.utc)

if last_modified_f3.date() == today.date():
    print(f"The file {product_data} was uploaded today ({last_modified_f3.date()}).")
else:
    print(f"The file {product_data} was uploaded on {last_modified_f3.date()}, not today.")
