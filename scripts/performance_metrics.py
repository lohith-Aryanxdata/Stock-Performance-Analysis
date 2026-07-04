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

df["Daily_Return"] = df["Close"].pct_change() * 100

print(df[["Date", "Close", "Daily_Return"]].head(10))

print("\nBest Day")
print(df.loc[df["Daily_Return"].idxmax()])

print("\nWorst Day")
print(df.loc[df["Daily_Return"].idxmin()])

df["MA_50"] = df["Close"].rolling(window=50).mean()

print("\nMoving Average")
print(df[["Date", "Close", "MA_50"]].tail())