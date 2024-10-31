import boto3
from openpyxl import load_workbook
import boto3,os
import pandas as pd 


s3_client= boto3.client('s3')
s3= boto3.resource('s3')

bucket_name = 'sales--data-etl'

objectdf1= s3_client.get_object(Bucket=bucket_name,Key='sales_data.csv') 
SalesDf=pd.read_csv(objectdf1['Body'])
print(SalesDf) 

objectdf2= s3_client.get_object(Bucket=bucket_name,Key='customer_data.json') 
CustomerDf=pd.read_json(objectdf2['Body'])
print(SalesDf) 

objectdf3= s3_client.get_object(Bucket=bucket_name,Key='product_data.xlsx') 
ProductDf=pd.read_excel(objectdf3['Body'])
print(ProductDf) 
