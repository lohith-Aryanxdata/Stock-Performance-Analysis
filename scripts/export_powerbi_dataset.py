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

query = """
SELECT
    Date,
    Ticker,
    Close,
    Volume
FROM stock_prices
"""

df = pd.read_sql(query, engine)

df.to_csv(
    "powerbi/powerbi_stock_dataset.csv",
    index=False
)

print("Power BI dataset exported successfully!")