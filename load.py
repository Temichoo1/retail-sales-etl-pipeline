#from sqlalchemy import create_engine
#
#def load_data(fact_sales, dim_store, dim_date, dim_feature):
#    
#    db_name = 'retail_project'
#    db_host = 'TEMITOPE\SQLEXPRESS'
#    db_port = 5432
#    db_password = 'My Password'
#    db_user = 'postgres'
#    
#    engine = create_engine(f'postgressql+{db_user}:{db_password}@db_host:{db_port}/{db_name}')
#    
#    
#    dim_store.to_sql('dim_store',
#                     engine,
#                     schemas = 'public',
#                     if_exists = 'replace',
#                     index = False )
#    
#    dim_date.to_sql('dim_date',
#                     engine,
#                     schemas = 'public',
#                     if_exists = 'replace',
#                     index = False )
#    
#    dim_feature.to_sql('dim_feature',
#                     engine,
#                     schemas = 'public',
#                     if_exists = 'replace',
#                     index = False )
#
#    fact_sales.to_sql('fact_sales',
#                     engine,
#                     schemas = 'public',
#                     if_exists = 'replace',
#                     index = False )
#    
#    print('Data loaded to postgres successfully')


from sqlalchemy import create_engine
import urllib

def load_data(fact_sales, dim_store, dim_date, dim_feature):

    # SQL Server details
    server = r'TEMITOPE\SQLEXPRESS'
    database = 'retail_project'

    # Windows Authentication
    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )

    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    # Load Dimension Tables
    dim_store.to_sql(
        'dim_store',
        con=engine,
        schema='dbo',
        if_exists='replace',
        index=False
    )

    dim_date.to_sql(
        'dim_date',
        con=engine,
        schema='dbo',
        if_exists='replace',
        index=False
    )

    dim_feature.to_sql(
        'dim_feature',
        con=engine,
        schema='dbo',
        if_exists='replace',
        index=False
    )

    # Load Fact Table
    fact_sales.to_sql(
        'fact_sales',
        con=engine,
        schema='dbo',
        if_exists='replace',
        index=False,
        chunksize = 1000
    )

    print("Data loaded to SQL Server successfully")