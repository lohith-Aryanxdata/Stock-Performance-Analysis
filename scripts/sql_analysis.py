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

query = """
SELECT *
FROM stock_prices
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.shape)

print("\nDataset Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())