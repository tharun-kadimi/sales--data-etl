from Extract import salesData ,customerData, productsData

sales_data='sales_data.csv'
customer_data='customer_data.json'
product_data='product_data.xlsx'

salesDf= salesData(sales_data) 

customerDf= customerData(customer_data)

productsDf= productsData(product_data)