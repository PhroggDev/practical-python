# pcost.py
#
# Exercise 1.33
import csv
import sys


def portfolioCost(filename):
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
# print(f'Total cost: {portfolioCost('Data/portfolio.csv'):.2f}')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '../Data/portfolio.csv'
cost = portfolioCost(filename)
print(f'Total cost: {cost}')
