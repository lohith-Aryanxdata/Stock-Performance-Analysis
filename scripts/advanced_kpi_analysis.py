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

df["Date"] = pd.to_datetime(df["Date"])

results = []

for ticker in df["Ticker"].unique():

    stock_df = df[df["Ticker"] == ticker].copy()

    stock_df["Daily_Return"] = (
        stock_df["Close"].pct_change()
    ) * 100

    avg_return = stock_df["Daily_Return"].mean()

    volatility = stock_df["Daily_Return"].std()

    best_day = stock_df["Daily_Return"].max()

    worst_day = stock_df["Daily_Return"].min()

    total_return = (
        (
            stock_df["Close"].iloc[-1]
            - stock_df["Close"].iloc[0]
        )
        / stock_df["Close"].iloc[0]
    ) * 100

    results.append([
        ticker,
        round(avg_return, 2),
        round(volatility, 2),
        round(best_day, 2),
        round(worst_day, 2),
        round(total_return, 2)
    ])

performance_df = pd.DataFrame(
    results,
    columns=[
        "Ticker",
        "Avg Daily Return %",
        "Volatility %",
        "Best Day %",
        "Worst Day %",
        "Total Return %"
    ]
)

print(performance_df)