from Extract import common_extraction
import pandas as pd 
sales_data='sales_data.csv'
customer_data='customer_data.json'
product_data='product_data.xlsx'
bucket_name = 'sales--data-etl'

salesDf= common_extraction(bucket_name,sales_data)
customerDf= common_extraction(bucket_name,customer_data)
productsDf= common_extraction(bucket_name,product_data) 

def export_sales_data():
    salesDf['transaction_date'] = pd.to_datetime(salesDf['transaction_date'], errors='coerce')
    # print(salesDf)
    salesDf['day']=salesDf['transaction_date'].dt.day
    sales_data_first_10_days=salesDf[(salesDf['day']>1) & (salesDf['day']<10)].sort_values('day')
    sales_data_first_10_days.drop(columns='day' ,inplace=True)
    # print(sales_data_first_10_days)
    return sales_data_first_10_days 