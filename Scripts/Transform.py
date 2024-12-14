from Extract import common_extraction

sales_data='sales_data.csv'
customer_data='customer_data.json'
product_data='product_data.xlsx'
bucket_name = 'sales--data-etl'

salesDf= common_extraction(bucket_name,sales_data)
customerDf= common_extraction(bucket_name,customer_data)
productsDf= common_extraction(bucket_name,product_data) 