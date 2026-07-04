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

    stock_df["Daily_Return"] = (
        stock_df["Close"].pct_change()
    ) * 100

    volatility = stock_df["Daily_Return"].std()

    avg_return = stock_df["Daily_Return"].mean()

    results.append([
        ticker,
        round(avg_return, 2),
        round(volatility, 2)
    ])

volatility_df = pd.DataFrame(
    results,
    columns=[
        "Ticker",
        "Average Daily Return %",
        "Volatility %"
    ]
)

print("\nVolatility Analysis")
print(volatility_df)

print("\nMost Volatile Stock")
print(
    volatility_df.loc[
        volatility_df["Volatility %"].idxmax()
    ]
)

print("\nLeast Volatile Stock")
print(
    volatility_df.loc[
        volatility_df["Volatility %"].idxmin()
    ]
)