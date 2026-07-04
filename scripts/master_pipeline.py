import os

print("STEP 1 - Downloading Stock Data")
os.system("python scripts/download_stock.py")

print("\nSTEP 2 - Loading Data to MySQL")
os.system("python scripts/load_to_mysql.py")

print("\nSTEP 3 - Validating Data")
os.system("python scripts/validate_data.py")

print("\nSTEP 4 - Generating Summary Report")
os.system("python scripts/summary_report.py")

print("\nPipeline Completed Successfully!")