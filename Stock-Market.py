import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data from Yahoo Finance."""
    stock = yf.download(ticker, start=start_date, end=end_date)
    return stock

def analyze_stock_data(stock):
    """Perform basic analysis on stock data."""
    print("Stock Data Overview:\n", stock.info())
    print("\nSummary Statistics:\n", stock.describe())
    print("\nMissing Values:\n", stock.isnull().sum())

def visualize_stock_data(stock, ticker):
    """Generate visualizations for stock price trends."""
    plt.figure(figsize=(12,6))
    plt.plot(stock['Close'], label=f'{ticker} Closing Price', color='blue')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.title(f'{ticker} Stock Price Trend')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol (e.g., AAPL): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    analyze_stock_data(stock_data)
    visualize_stock_data(stock_data, ticker)
