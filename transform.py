import pandas as pd

#transforming into fact and dimension tables

def transform_data(features_df, sales_df,stores_df):
      features_df['Date'] = pd.to_datetime(features_df['Date']) #converting to date time
      sales_df['Date'] = pd.to_datetime(sales_df['Date'], dayfirst = True)
      
      #list of columns to drop, adding them to a list
      markdown_colms = ['MarkDown1', 'MarkDown2','MarkDown3','MarkDown4','MarkDown5']
      features_df = features_df.drop(columns = markdown_colms, errors = 'ignore')
      
                #####CREATING TABLES########
      #Creating Dim store
      dim_store = stores_df.drop_duplicates().reset_index(drop = True)
      
      #creating dim dates
      dim_date = sales_df[['Date', 'IsHoliday']].drop_duplicates().copy()
      
      #creating new columns in the Dim_date table
      dim_date['year'] = dim_date['Date'].dt.year
      dim_date['month'] = dim_date['Date'].dt.month
      #dim_date['Week'] = dim_date['Date'].dt.isocalender().week.astype(int)
      dim_date['Week'] = dim_date['Date'].dt.isocalendar().week
      
      #Creating Dim Featire table
      dim_feature = features_df.drop_duplicates().reset_index(drop = True)
      
      #Creating fact.Sales table
      fact_sales = sales_df.copy()
      
      def normalise(df):
          df.columns = df.columns.str.lower()#.str.replace('', '_')
          return df
      dim_date = normalise(dim_date)
      dim_feature = normalise(dim_feature)
      dim_store = normalise(dim_store)
      fact_sales = normalise(fact_sales)
      
      return fact_sales, dim_store, dim_date, dim_feature
