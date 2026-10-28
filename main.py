from extract import extract_data
from transform import transform_data
from load import load_data


def run_pipeline():
    try:
        print("SQL Server ETL Pipeline Started...")

        # Extract
        features_df, sales_df, stores_df = extract_data()

        # Transform
        fact_sales, dim_store, dim_date, dim_feature = transform_data(
            features_df,
            sales_df,
            stores_df
        )

        # Load into SQL Server
        load_data(
            fact_sales,
            dim_store,
            dim_date,
            dim_feature
        )

        print("Pipeline completed successfully. Data loaded into SQL Server.")

    except Exception as e:
        print(f"Pipeline failed: {e}")


if __name__ == "__main__":
    run_pipeline()
