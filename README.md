# Order Book Anaysis
A python project that analyzes the order book of a cryptocurrency exchange to gain insights into market liquidity and trading activity.

__Note:__ You have the required libraries ```requests```, ```pandas```, ```matplotlib``` installed before running the code. You can install them using the following commands:
```
pip install requests
pip install pandas
pip install matplotlib
```
__1. Data Retrieval:__

 - The ```fetch_order_book_data``` method fetches order book data from the specified API using the ```requests``` library and stores it in the ```self.data``` variable.

__2. Data Analysis:__

 - The ```analyze_order_book_data``` method converts the data to a pandas DataFrame for analysis.
 - The DataFrame is processed to calculate the cumulative sum of quantities for bid and ask sides.
 - Visualizations are generated using ```matplotlib``` to show the order book depth and liquidity.
