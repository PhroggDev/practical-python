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
# print(f"Total cost: {portfolioCost('Data/portfolio.csv'):.2f}")
# Now once again with csv missing values to see if we throw the error in the function
print(f"Total cost: {portfolioCost('Data/missing.csv'):.2f}")
