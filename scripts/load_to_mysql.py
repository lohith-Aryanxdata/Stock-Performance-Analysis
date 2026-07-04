import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("ARYAN.sql@123")
host = "localhost"
database = "stock_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Read CSV
df = pd.read_csv("data/stocks.csv")

print("First 5 Rows")
print(df.head())

print("\nFirst 10 Rows")
print(df.head(10))

print("\nColumns")
print(df.columns)

# Load into MySQL
df.to_sql(
    name="stock_prices",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")