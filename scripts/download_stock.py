import yfinance as yf
import pandas as pd

stocks = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "TSLA"
]

all_data = []

for stock in stocks:

    df = yf.download(
        stock,
        period="1y"
    )

    df.columns = df.columns.get_level_values(0)
    df.columns.name = None

    df.reset_index(inplace=True)

    df["Ticker"] = stock

    all_data.append(df)

final_df = pd.concat(
    all_data,
    ignore_index=True
)

print(final_df.head())

final_df.to_csv(
    "data/stocks.csv",
    index=False
)

print("Multi-stock CSV saved successfully!")