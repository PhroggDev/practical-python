# pcost.py
#
# Exercise 2.15
def portfolioCost(filename):
    totalCost = 0
    with open(filename, 'rt') as f:
        # headers = next(f).split(',')
        rows = f.read()
    for rowno, row in enumerate(rows, start=1):
        try:
            nshares = int(row[1])
            price = float(row[2])
            totalCost += nshares * price
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
            next(f)

    return totalCost


print(f"Total cost: {portfolioCost('Data/portfolio.csv'):.2f}")
