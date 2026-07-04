/* =====================================
   STOCK PERFORMANCE PROJECT
   SQL QUERIES
   ===================================== */


/* Create Database */

CREATE DATABASE stock_analysis;


/* Select Database */

USE stock_analysis;


/* Show All Databases */

SHOW DATABASES;


/* Show Tables */

SHOW TABLES;


/* View Entire Table */

SELECT *
FROM stock_prices;


/* View First 10 Rows */

SELECT *
FROM stock_prices
LIMIT 10;


/* Count Total Records */

SELECT COUNT(*)
FROM stock_prices;


/* Count Records Per Stock */

SELECT
    Ticker,
    COUNT(*) AS Total_Records
FROM stock_prices
GROUP BY Ticker;


/* Check Date Range Per Stock */

SELECT
    Ticker,
    MIN(Date) AS Start_Date,
    MAX(Date) AS End_Date
FROM stock_prices
GROUP BY Ticker;


/* Average Closing Price Per Stock */

SELECT
    Ticker,
    AVG(Close) AS Avg_Close
FROM stock_prices
GROUP BY Ticker;


/* Highest Closing Price Per Stock */

SELECT
    Ticker,
    MAX(Close) AS Highest_Close
FROM stock_prices
GROUP BY Ticker;


/* Lowest Closing Price Per Stock */

SELECT
    Ticker,
    MIN(Close) AS Lowest_Close
FROM stock_prices
GROUP BY Ticker;


/* Average Volume Per Stock */

SELECT
    Ticker,
    AVG(Volume) AS Avg_Volume
FROM stock_prices
GROUP BY Ticker;


/* Maximum Volume Per Stock */

SELECT
    Ticker,
    MAX(Volume) AS Max_Volume
FROM stock_prices
GROUP BY Ticker;


/* Sort Stocks By Average Close */

SELECT
    Ticker,
    AVG(Close) AS Avg_Close
FROM stock_prices
GROUP BY Ticker
ORDER BY Avg_Close DESC;


/* Sort Stocks By Average Volume */

SELECT
    Ticker,
    AVG(Volume) AS Avg_Volume
FROM stock_prices
GROUP BY Ticker
ORDER BY Avg_Volume DESC;


/* Latest Price Per Stock */

SELECT
    Ticker,
    Date,
    Close
FROM stock_prices
ORDER BY Date DESC;


/* Check For Missing Close Values */

SELECT *
FROM stock_prices
WHERE Close IS NULL;


/* Check For Missing Volume Values */

SELECT *
FROM stock_prices
WHERE Volume IS NULL;


/* Check For Duplicate Records */

SELECT
    Date,
    Ticker,
    COUNT(*) AS Duplicate_Count
FROM stock_prices
GROUP BY
    Date,
    Ticker
HAVING COUNT(*) > 1;


/* View Specific Stock */

SELECT *
FROM stock_prices
WHERE Ticker = 'AAPL';


/* View Specific Date Range */

SELECT *
FROM stock_prices
WHERE Date BETWEEN
'2025-06-20'
AND
'2025-12-31';


/* Average Price By Stock */

SELECT
    Ticker,
    ROUND(AVG(Close), 2) AS Avg_Close
FROM stock_prices
GROUP BY Ticker;


/* Total Records Validation */

SELECT COUNT(*) AS Total_Rows
FROM stock_prices;


/* Unique Stocks Validation */

SELECT DISTINCT Ticker
FROM stock_prices;


/* Stock Summary */

SELECT
    Ticker,
    COUNT(*) AS Records,
    ROUND(AVG(Close), 2) AS Avg_Close,
    ROUND(MIN(Close), 2) AS Min_Close,
    ROUND(MAX(Close), 2) AS Max_Close,
    ROUND(AVG(Volume), 0) AS Avg_Volume
FROM stock_prices
GROUP BY Ticker;