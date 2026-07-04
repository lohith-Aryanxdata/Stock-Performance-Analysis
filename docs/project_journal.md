# Stock Performance Analysis Project

## Day 1 - Project Setup & Data Extraction

### Objective
Set up the project environment and download stock market data using Python.

### Tasks Completed

- Created project folder structure
- Opened project in VS Code
- Created and activated virtual environment
- Installed required Python libraries:
  - yfinance
  - pandas
  - matplotlib
  - seaborn
- Downloaded 1 year of Apple (AAPL) stock data from Yahoo Finance
- Explored the downloaded dataset
- Checked:
  - Shape of data
  - Columns
  - Data types
- Calculated:
  - Highest closing price
  - Lowest closing price
  - Average closing price
- Exported dataset to CSV

### Files Created

- scripts/download_stock.py
- data/apple_stock.csv

### Key Learnings

- What a virtual environment is
- How to install Python packages
- How to use the yfinance library
- What a Pandas DataFrame is
- How to save data as a CSV file

### Challenges Faced

- PowerShell execution policy prevented virtual environment activation
- Resolved by updating execution policy and activating the environment successfully

### Next Steps

- Create MySQL database
- Design stock_prices table
- Connect Python to MySQL
- Load stock data into database
- Learn basic SQL queries
# Day 2

## Objective
Store stock market data in a MySQL database and connect Python to MySQL.

## Completed Tasks

- Created MySQL database: stock_analysis
- Installed SQLAlchemy and PyMySQL
- Created a Python connection to MySQL
- Resolved connection and interpreter issues
- Read stock data from CSV
- Loaded data into MySQL table: stock_prices
- Verified successful data load

## Key Learnings

- How Python connects to MySQL
- What SQLAlchemy does
- How to load a Pandas DataFrame into a database
- Difference between CSV storage and database storage

## Next Steps

- Learn SQL queries
- Analyze stock data using SQL
- Perform EDA in Python
- Prepare data for Power BI

# Day 3 Progress

Today's focus was integrating SQL analysis with Python and performing stock performance calculations.

Completed tasks:

- Retrieved stock data from MySQL using SQLAlchemy
- Loaded SQL query results into a Pandas DataFrame
- Performed exploratory data analysis using:
  - head()
  - shape
  - info()
  - describe()
- Created stock price visualization using Matplotlib
- Calculated Daily Returns
- Identified Best Trading Day
- Identified Worst Trading Day
- Calculated 50-Day Moving Average

Key Learning:
Learned how Python, SQL, and data visualization tools work together in a complete analytics workflow. Also gained understanding of stock performance metrics commonly used in financial analysis.

# Day 4 Progress 
Objectives Completed:
1. KPI Analysis Script Development
Created kpi_analysis.py to calculate stock performance metrics from MySQL data.
Calculated:
Average Closing Price
Highest Closing Price
Lowest Closing Price
Average Trading Volume
Total Return Percentage

2. Troubleshooting & Environment Fixes
Resolved multiple development environment issues:
Virtual environment activation problems
Missing package errors (pandas, sqlalchemy)
MySQL connection string formatting issues
Database authentication errors
Incorrect table name references

3. Moving Average Analysis:
Created moving_average_chart.py.
Implemented:
20-Day Moving Average calculation using Pandas rolling window.
Stock Close Price trend visualization.
Moving Average trend visualization.

4. Data Visualization Improvements:
Fixed chart readability issues:
Converted Date column to proper datetime format.
Rotated x-axis labels for better visibility.
Added gridlines.
Applied tight_layout() for cleaner presentation.
Improved chart sizing for large datasets.

5. Data Pipeline Refactoring:
Refactored download_stock.py.
Cleaned Yahoo Finance multi-level column structure.
Reset Date index into a standard column.
Saved clean CSV output for downstream processing.
Standardized dataset structure for future multi-stock support.
# Day 5 Progress 
Multi-Stock Data Engineering

Tasks Completed

Backed up project before major modifications.
Modified stock download pipeline to support multiple tickers.
Added Apple (AAPL), Microsoft (MSFT), Google (GOOGL), Amazon (AMZN), and Tesla (TSLA).
Introduced Ticker column to dataset.
Re-downloaded and validated one year of historical stock data.
Reloaded cleaned data into MySQL.
Verified row counts and database structure.
Created validation script to check:
Missing values
Available tickers
Record counts per stock
Dataset dimensions

Key Learning

Learned how to scale a pipeline from a single stock to multiple entities using a unified schema.
Understood why data validation is a critical step before analytics and reporting.

## Day 6 Progress

Objective:
Extend project from single-stock analysis to multi-stock analysis.

 Tasks Completed:
- Added AMZN and TSLA to stock universe
- Refactored download script for multiple tickers
- Combined stock data into one CSV
- Loaded multi-stock data into MySQL
- Updated validation script
- Created multi-stock KPI analysis
- Created return comparison visualization
- Tested complete ETL pipeline

Outcome:
Project now supports portfolio-level stock analysis across 5 companies.
## Day 7 Progress
Objectives
Perform advanced stock performance analysis.
Build volatility metrics and visualizations.
Create a consolidated reporting dataset.
Automate the end-to-end data pipeline.
Prepare data for Power BI integration.
Tasks Completed
1. Advanced KPI Analysis

Created an advanced KPI analysis script to evaluate performance across all five stocks (AAPL, MSFT, GOOGL, AMZN, TSLA).

Metrics calculated:

Average Closing Price
Average Daily Return
Total Return Percentage
Average Trading Volume
Volatility Percentage
2. Volatility Analysis

Created a volatility analysis script to measure stock risk using daily return standard deviation.

Outputs:

Volatility percentage for each stock
Most volatile stock identification
Least volatile stock identification
3. Volatility Comparison Chart

Developed a visualization comparing volatility across all stocks using a bar chart.

Purpose:

Compare relative stock risk
Support future Power BI reporting
4. Summary Report Generation

Created a consolidated reporting script that combines key performance indicators into a single dataset.

Generated file:

stock_summary_report.csv

Included metrics:

Ticker
Average Close
Total Return %
Average Daily Return %
Volatility %
Average Volume
5. Master Pipeline Automation

Created a master pipeline script to automate project execution.

Pipeline workflow:

Download stock data
Load data into MySQL
Validate dataset
Generate summary report

This reduced the project workflow to a single command execution.

6. Power BI Dataset Export

Created an export script to generate a clean dataset for Power BI consumption.

Generated file:

powerbi_stock_dataset.csv

Included fields:

Date
Ticker
Close
Volume
7. SQL Documentation Cleanup

Organized project SQL assets.

Actions:

Created project_queries.sql
Consolidated useful SQL queries used throughout the project
Planned migration of SQL-related documentation into the dedicated SQL folder
8. Project Validation

Executed the complete pipeline successfully.

Validation results:

Total records loaded: 1,255
Stocks loaded: 5
Records per stock: 251
Missing values: 0
Duplicate records: 0
Key Findings
Performance Ranking
GOOGL – 121.48% Return
AAPL – 48.85% Return
TSLA – 24.31% Return
AMZN – 16.55% Return
MSFT – -19.89% Return
Volatility Ranking
TSLA – 2.80% (Highest Volatility)
AMZN – 1.93%
GOOGL – 1.84%
MSFT – 1.63%
AAPL – 1.43% (Lowest Volatility)
Outcome

Successfully completed the advanced analytics phase and established an automated reporting pipeline. The project is now prepared for Power BI dashboard development, GitHub publishing, and final portfolio packaging.

## Day 8 Progress
