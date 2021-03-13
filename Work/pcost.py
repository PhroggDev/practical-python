# pcost.py
#
# Exercise 1.27
def portfolioCost(filename):
    totalCost = 0.0  # initiliaze a floating point variable
    with open(filename, 'rt') as f: # read in csv file
        headers = next(f)                 # grab the first line of headers
        for line in f:                    # loop thru lines and use values
            row = line.split(',')         # populate variables
            nshares = int(row[1])         # first value is number of shares
            price = float(row[2])         # 2nd value is price
            totalCost += nshares * price  # calculate cost of each stock and sum
    return totalCost