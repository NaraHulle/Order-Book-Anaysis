import requests
import pandas as pd
import matplotlib.pyplot as plt

class OrderBookAnalyzer:
    def __init__(self, api_url, symbol):
        self.api_url = api_url
        self.symbol = symbol
        self.data = None

    def fetch_order_book_data(self):
        # Fetch order book data from the API
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error fetching order book data from the API.")

    def analyze_order_book_data(self):
        # Convert data to pandas DataFrame for analysis
        df = pd.DataFrame(self.data, columns=['price', 'quantity'])

        # Convert price and quantity columns to numeric::
        df['price'] = pd.to_numeric(df['price'])
        df['quantity'] = pd.to_numeric(df['quantity'])

        # Calculate cumulative sum of quantities for bid and ask sides:
        df['bid_cumulative'] = df[df['quantity'] > 0]['quantity'].cumsum()
        df['ask_cumulative'] = df[df['quantity'] < 0]['quantity'].abs().cumsum()

        # Generate visualizations:
        self.generate_depth_chart(df)
        self.generate_liquidity_chart(df)

    def generate_depth_chart(self, df):
        # Generate depth chart showing bid and ask levels
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df['price'], df['bid_cumulative'], label='Bids')
        ax.plot(df['price'], df['ask_cumulative'], label='Asks')
        ax.set_title(f'{self.symbol} Order Book Depth')
        ax.set_xlabel('Price')
        ax.set_ylabel('Cumulative Quantity')
        ax.legend()
        plt.show()

    def generate_liquidity_chart(self, df):
        # Generate liquidity chart showing bid and ask volumes
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(df['price'], df['quantity'], width=0.1, align='edge')
        ax.set_title(f'{self.symbol} Order Book Liquidity')
        ax.set_xlabel('Price')
        ax.set_ylabel('Quantity')
        plt.show()

# Example usage:

# Define API URL and symbol:
api_url = "https://api.example.com/order-book"
symbol = "BTC/USD"

# Create an instance of OrderBookAnalyzer
analyzer = OrderBookAnalyzer(api_url, symbol)

# Fetch order book data
analyzer.fetch_order_book_data()

# Analyze and visualize order book data
analyzer.analyze_order_book_data()
