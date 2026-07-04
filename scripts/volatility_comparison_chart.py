import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import matplotlib.pyplot as plt

username = "root"
password = quote_plus("ARYAN.sql@123")
host = "localhost"
database = "stock_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

query = "SELECT * FROM stock_prices"

df = pd.read_sql(query, engine)

results = []

for ticker in df["Ticker"].unique():

    stock_df = (
        df[df["Ticker"] == ticker]
        .copy()
        .sort_values("Date")
    )

    stock_df["Daily_Return"] = (
        stock_df["Close"].pct_change()
    ) * 100

    volatility = stock_df["Daily_Return"].std()

    results.append([
        ticker,
        volatility
    ])

volatility_df = pd.DataFrame(
    results,
    columns=[
        "Ticker",
        "Volatility"
    ]
)

plt.figure(figsize=(10,6))

plt.bar(
    volatility_df["Ticker"],
    volatility_df["Volatility"]
)

plt.title("Stock Volatility Comparison")
plt.xlabel("Ticker")
plt.ylabel("Volatility %")

plt.grid(axis="y")

plt.tight_layout()

plt.show()