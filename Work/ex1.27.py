# pcost.py
totalCost = 0.0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        totalCost += nshares * price

print(f"Total cost of portfolio: {totalCost}")