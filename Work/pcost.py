# pcost.py
#
# Exercise 2.4
import csv
import sys


def portfolio_cost(filename):
    '''Computes total cost (shares x price) of a portfolio file'''
    total_cost = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

# print(f'Total cost: {portfolio_cost('Data/portfolio.csv'):.2f}')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
