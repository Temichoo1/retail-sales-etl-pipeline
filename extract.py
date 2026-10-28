import pandas as pd

def extract_data():
    features_df = pd.read_csv(r'C:\Users\tadej\OneDrive\Documents\Python\ETLs\Data Network\data\csv\Features_dataset.csv')
    sales_df = pd.read_csv(r'C:\Users\tadej\OneDrive\Documents\Python\ETLs\Data Network\data\csv\sales_dataset.csv')
    stores_df = pd.read_csv(r'C:\Users\tadej\OneDrive\Documents\Python\ETLs\Data Network\data\csv\stores_dataset.csv')
    
    print('Features dataset')
    print(features_df.head())
    print(features_df.dtypes)
    
    print('Sales dataset')
    print(sales_df.head())
    print(sales_df.dtypes)

    print('Stores dataset')
    print(stores_df.head())
    print(stores_df.dtypes)
    
#extract_data()
    return features_df, sales_df,stores_df