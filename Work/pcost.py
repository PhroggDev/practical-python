# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
        except ValueError:
            print('Missing or Bad value')
            next(rows)
    return total_cost

# print(f'Total cost: {portfolio_cost('Data/portfolio.csv'):.2f}')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
