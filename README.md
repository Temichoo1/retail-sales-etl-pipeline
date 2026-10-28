# retail-sales-etl-pipeline
# Retail ETL Pipeline

A production-style ETL (Extract, Transform, Load) pipeline built in Python that processes raw retail data and loads it into a structured PostgreSQL data warehouse using a star schema (fact and dimension tables).

---

## 🔍 Project Overview

[
This project simulates a real-world retail data engineering workflow. Raw CSV data from three sources — sales transactions, store information, and promotional features — is extracted, cleaned, transformed into an analytical schema, and loaded into PostgreSQL for downstream reporting and analysis.

---

## 🏗️ Architecture



```
Raw CSV Files
    │
    ▼
extract.py       → Loads raw data from CSV files into Pandas DataFrames
    │
    ▼
transform.py     → Cleans data, handles nulls, builds fact & dimension tables
    │
    ▼
load.py          → Loads transformed tables into PostgreSQL
    │
    ▼
main.py          → Orchestrates the full pipeline end-to-end
```

---

## 📁 Data Sources

[](https://github.com/Robin6551/retail-etl-project/blob/main/README.md#-data-sources)

|File|Description|
|---|---|
|`sales_dataset.csv`|Weekly sales transactions per store and department|
|`stores_dataset.csv`|Store metadata including type and size|
|`Features_dataset.csv`|External factors — temperature, fuel price, promotions, CPI, unemployment|

---

## ⚙️ Tech Stack

[](https://github.com/Robin6551/retail-etl-project/blob/main/README.md#️-tech-stack)

- **Python** — core pipeline logic
- **Pandas** — data extraction and transformation
- **SQL** — data warehouse destination
- **SQLAlchemy** — database connection and loading

---

## 🗄️ Data Warehouse Schema (Star Schema)

[](https://github.com/Robin6551/retail-etl-project/blob/main/README.md#️-data-warehouse-schema-star-schema)

**Fact Table:**

- `fact_sales` — weekly sales per store and department

**Dimension Tables:**

- `dim_store` — store type and size
- `dim_date` — date breakdowns (week, month, year, holiday flag)
- `dim_features` — economic indicators and promotional markdowns
