# pcost.py
#
# Exercise 1.31
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


# Once with good values
print("Using a known good CSV file:")
print(f"Total cost: {portfolioCost('Data/portfolio.csv'):.2f}")
print("=*="*17)
# Now once again with csv missing values to see if we throw the error in the function
print("Using a CSV file with a missing or malformed entry:")
print(f"Total cost: {portfolioCost('Data/missing.csv'):.2f}")
