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

results = []

for ticker in df["Ticker"].unique():

    stock_df = (
        df[df["Ticker"] == ticker]
        .copy()
        .sort_values("Date")
    )

    # Daily Return
    stock_df["Daily_Return"] = (
        stock_df["Close"].pct_change()
    ) * 100

    # KPIs
    avg_close = stock_df["Close"].mean()

    total_return = (
        (
            stock_df["Close"].iloc[-1]
            - stock_df["Close"].iloc[0]
        )
        / stock_df["Close"].iloc[0]
    ) * 100

    avg_daily_return = (
        stock_df["Daily_Return"].mean()
    )

    volatility = (
        stock_df["Daily_Return"].std()
    )

    avg_volume = (
        stock_df["Volume"].mean()
    )

    results.append([
        ticker,
        round(avg_close, 2),
        round(total_return, 2),
        round(avg_daily_return, 2),
        round(volatility, 2),
        round(avg_volume, 0)
    ])

summary_df = pd.DataFrame(
    results,
    columns=[
        "Ticker",
        "Average Close",
        "Total Return %",
        "Average Daily Return %",
        "Volatility %",
        "Average Volume"
    ]
)

print("\nStock Performance Summary")
print(summary_df)

summary_df.to_csv(
    "data/stock_summary_report.csv",
    index=False
)

print("\nSummary report saved successfully!")