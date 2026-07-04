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

print("\n===== STOCK KPI SUMMARY =====\n")

results = []

for ticker in df["Ticker"].unique():

    stock_df = df[df["Ticker"] == ticker]

    avg_close = stock_df["Close"].mean()

    highest_close = stock_df["Close"].max()

    lowest_close = stock_df["Close"].min()

    avg_volume = stock_df["Volume"].mean()

    total_return = (
        (
            stock_df["Close"].iloc[-1]
            - stock_df["Close"].iloc[0]
        )
        / stock_df["Close"].iloc[0]
    ) * 100

    print(f"Ticker: {ticker}")
    print(f"Average Close: {avg_close:.2f}")
    print(f"Highest Close: {highest_close:.2f}")
    print(f"Lowest Close: {lowest_close:.2f}")
    print(f"Average Volume: {avg_volume:,.0f}")
    print(f"Total Return %: {total_return:.2f}")
    print("-" * 40)

    results.append(
        [
            ticker,
            avg_close,
            highest_close,
            lowest_close,
            avg_volume,
            total_return
        ]
    )

performance_df = pd.DataFrame(
    results,
    columns=[
        "Ticker",
        "Average_Close",
        "Highest_Close",
        "Lowest_Close",
        "Average_Volume",
        "Return"
    ]
)

print("\n===== PERFORMANCE TABLE =====\n")
print(performance_df)

print("\n===== BEST PERFORMER =====\n")
print(
    performance_df.sort_values(
        by="Return",
        ascending=False
    ).head(1)
)

print("\n===== WORST PERFORMER =====\n")
print(
    performance_df.sort_values(
        by="Return",
        ascending=True
    ).head(1)
)