# pcost.py
#
# Exercise 2.4
import csv
import sys


def portfolio_cost(filename):
    total = 0
    with open(filename, "rt") as f:
        headers = next(f).split(",")
        for line in f:
            row = line.split(",")
            nshares = int(row[1])
            price = float(row[2])
            total += nshares * price
    return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost of portfolio:", cost)
