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

query = "SELECT * FROM stock_prices"
df = pd.read_sql(query, engine)

print("\nAverage Close")
print(df["Close"].mean())

print("\nHighest Close")
print(df["Close"].max())

print("\nLowest Close")
print(df["Close"].min())

print("\nAverage Volume")
print(df["Volume"].mean())

total_return = (
    (df["Close"].iloc[-1] - df["Close"].iloc[0])
    / df["Close"].iloc[0]
) * 100

print("\nTotal Return %")
print(round(total_return, 2))

df["Daily_Return"] = df["Close"].pct_change()

volatility = (
    df["Daily_Return"].std()
) * 100

print("\nVolatility")
print(round(volatility, 2))