# pcost.py
#
# Exercise 2.15
import csv


def portfolioCost(filename):
    totalCost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                totalCost += nshares * price
                # Catch errors in above int() or float() conversions
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                next(f)

    return totalCost


# print(f"Total cost: {portfolioCost('Data/portfolio.csv'):.2f}")
