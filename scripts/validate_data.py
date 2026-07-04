import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Database Connection
username = "root"
password = quote_plus("ARYAN.sql@123")
host = "localhost"
database = "stock_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Read Data
query = "SELECT * FROM stock_prices"
df = pd.read_sql(query, engine)

# Basic Dataset Information
print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMNS ==========")
print(df.columns.tolist())

# Missing Values Check
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Duplicate Check
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Stock Validation
print("\n========== STOCKS LOADED ==========")
print(df["Ticker"].unique())

print("\n========== RECORDS PER STOCK ==========")
print(df.groupby("Ticker").size())

# Date Range Per Stock
print("\n========== DATE RANGE PER STOCK ==========")

df["Date"] = pd.to_datetime(df["Date"])

date_summary = (
    df.groupby("Ticker")
      .agg(
          Start_Date=("Date", "min"),
          End_Date=("Date", "max"),
          Records=("Date", "count")
      )
)

print(date_summary)

# Price Validation
print("\n========== PRICE SUMMARY ==========")

price_summary = (
    df.groupby("Ticker")
      .agg(
          Min_Close=("Close", "min"),
          Max_Close=("Close", "max"),
          Avg_Close=("Close", "mean")
      )
)

print(price_summary.round(2))

# Volume Validation
print("\n========== VOLUME SUMMARY ==========")

volume_summary = (
    df.groupby("Ticker")
      .agg(
          Avg_Volume=("Volume", "mean"),
          Max_Volume=("Volume", "max")
      )
)

print(volume_summary.round(0))

print("\n========== VALIDATION COMPLETE ==========")