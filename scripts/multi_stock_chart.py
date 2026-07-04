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

plt.figure(figsize=(15,7))

for ticker in df["Ticker"].unique():

    stock_df = df[df["Ticker"] == ticker]

    plt.plot(
        stock_df["Date"],
        stock_df["Close"],
        label=ticker
    )

plt.title("Stock Price Comparison")

plt.xlabel("Date")
plt.ylabel("Close Price")

plt.legend()

plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()