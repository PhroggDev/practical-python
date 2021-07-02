# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    """
    Read a stock portfolio from a csv file into a list of dictionary entries including name, # of shares, and current price
    """
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(stock)
    return portfolio

def read_prices(filename):
    """
    Read a csv file of price data into a dictionary mapping of names to prices
    """
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

# check if the files with price data are cli parameters
# set default test data if not passed to script
if len(sys.argv) == 3:
    filename1 = sys.argv[1]
    filename1 = sys.argv[2]
else:
    filename1 = 'Data/portfolio.csv'
    filename2 = 'Data/prices.csv'

portfolio = read_portfolio(filename1)
prices = read_prices(filename2)

# print value of portfolio followed by value of price list
totalCost = 0.0
for s in portfolio:
    totalCost += s['shares'] * s['price']
print(f"Total cost of Portfolio: {totalCost:.2f}")
totalValue = 0.0
for s in portfolio:
    totalValue += s['shares'] * prices[s['name']]
print(f"Current Value of Portfolio: {totalValue:.2f}")
print(f"Gain/Loss: {totalValue - totalCost:.2f}")
