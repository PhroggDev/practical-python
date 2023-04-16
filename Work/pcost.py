# pcost.py
import csv
import sys

def portfolio_cost(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    totalCost = 0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                nshares = int(row[1])
                price = float(row[2])
                totalCost += nshares * price
        except ValueError:
            print('Missing or Bad value')
            next(rows)
    return totalCost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
