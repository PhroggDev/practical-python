# pcost.py
#
# Exercise 1.33
# Reading file name(s) from the cli
import csv
import sys


def portfolioCost(filename):
    totalCost = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        try:
            for line in f:
                row = line.split(',')
                nshares = int(row[1])
                price = float(row[2])
                totalCost += nshares * price
        except ValueError:
            print('Missing or Bad value')
            next(f)
    return totalCost


f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
for row in rows:
    print(row)
f.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"     # default file

cost = portfolio_cost(filename)
print("Total cost:", cost)
