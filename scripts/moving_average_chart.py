import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

username = "root"
password = quote_plus("ARYAN.sql@123")
host = "localhost"
database = "stock_analysis"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

query = "SELECT * FROM stock_prices"

df = pd.read_sql(query, engine)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate 20-Day Moving Average
df["MA20"] = df["Close"].rolling(window=20).mean()

# Create chart
plt.figure(figsize=(15, 7))

plt.plot(
    df["Date"],
    df["Close"],
    label="Close Price"
)

plt.plot(
    df["Date"],
    df["MA20"],
    label="20-Day Moving Average"
)

plt.title("Apple Stock Price vs 20-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price ($)")

# Show one label per month
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

plt.xticks(rotation=45)

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()