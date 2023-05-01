# report.py
#
# Exercise 2.5
import csv
def read_portfolio(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)
    return portfolio


# Exercise 2.6
def read_prices(filename):
    """Update data object with 'current' list of prices from file"""
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            # print(row)
            try:
                key = row[0]
                val = row[1]
                # print(f"Key: {key} Val: {val}")
                prices[key] = float(val)
            except:
                continue
    return prices
