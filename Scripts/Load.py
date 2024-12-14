from Transform import export_sales_data
import oracledb
from  sqlalchemy import create_engine,text
import configparser
import pandas as pd 

def get_db_connection():
    config = configparser.ConfigParser() 
    config.read(r'C:\Users\tharu\OneDrive\Desktop\sales--data--etl\sales--data-etl\Scripts\config.ini')
    user= config['database']['username']
    password=config['database']['password']
    host= config['database']['host']
    port=config['database']['port']
    service_name=config['database']['service_name']
    dsn_tns = oracledb.makedsn(host, port, service_name=service_name)
    engine = create_engine(f'oracle+oracledb://{user}:{password}@{dsn_tns}')
    return engine.connect()
    
def loading_sales_data():
    connection = get_db_connection()
    sales_df=export_sales_data()
    print(sales_df)
    sales_df.to_sql('sales31', con=connection, if_exists='append', index=False)
loading_sales_data()    