import yfinance as yf
from datetime import datetime
import pandas as pd
import os

# Define the ticker symbol
tickerSymbol = input("What company do you want to search for? ")

# Check if the CSV file already exists
if os.path.exists(f'{tickerSymbol}_data.csv'):
    # If the file exists, read the data from the file
    tickerDf = pd.read_csv(f'{tickerSymbol}_data.csv')
    tickerDf.set_index('Date', inplace=True)
else:
    # If the file doesn't exist, fetch the data and create the file

    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # Get the current date
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1h', start='2024-01-01', end=current_date)

    # Store the DataFrame to a CSV file
    tickerDf.to_csv(f'{tickerSymbol}_data.csv')

# Find the date with the highest "High" value
highest_high_date = tickerDf['High'].idxmax()

# Find the highest "High" value
highest_high_value = tickerDf['High'].max()

print("The highest 'High' value was on:", highest_high_date)
print("The highest 'High' value was:", highest_high_value)