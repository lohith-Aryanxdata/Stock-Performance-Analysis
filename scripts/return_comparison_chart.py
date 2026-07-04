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

    stock_df = df[df["Ticker"] == ticker]

    total_return = (
        (
            stock_df["Close"].iloc[-1]
            - stock_df["Close"].iloc[0]
        )
        / stock_df["Close"].iloc[0]
    ) * 100

    results.append([ticker, total_return])

performance_df = pd.DataFrame(
    results,
    columns=["Ticker", "Return"]
)

performance_df = performance_df.sort_values(
    by="Return",
    ascending=False
)

plt.figure(figsize=(10,6))

plt.bar(
    performance_df["Ticker"],
    performance_df["Return"]
)

plt.title("Total Return by Stock")

plt.xlabel("Ticker")
plt.ylabel("Return %")

plt.grid(True)

plt.tight_layout()

plt.show()