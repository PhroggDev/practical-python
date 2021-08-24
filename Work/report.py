# report.py
#
# Exercise 2.4
import csv
# import sys


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
        except ValueError:
            print('Missing or Bad value')
            next(rows)
    return portfolio
    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    # filename = 'Data/portfolio.csv'
