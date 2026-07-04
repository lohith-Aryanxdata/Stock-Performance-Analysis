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

volume_df = (
    df.groupby("Ticker")["Volume"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(10,6))

plt.bar(
    volume_df["Ticker"],
    volume_df["Volume"]
)

plt.title("Average Trading Volume")

plt.xlabel("Ticker")
plt.ylabel("Average Volume")

plt.grid(True)

plt.tight_layout()

plt.show()