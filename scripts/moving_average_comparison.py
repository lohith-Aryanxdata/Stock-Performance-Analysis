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

df["Date"] = pd.to_datetime(df["Date"])

stocks = ["AAPL", "MSFT", "GOOGL"]

plt.figure(figsize=(15,7))

for stock in stocks:

    stock_df = df[df["Ticker"] == stock].copy()

    stock_df["MA20"] = (
        stock_df["Close"]
        .rolling(window=20)
        .mean()
    )

    plt.plot(
        stock_df["Date"],
        stock_df["MA20"],
        label=f"{stock} MA20"
    )

plt.title("20-Day Moving Average Comparison")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()