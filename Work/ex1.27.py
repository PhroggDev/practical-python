# pcost.py
totalCost = 0.0 # initiliaze a floating point variable
with open('Data/portfolio.csv', 'rt') as f: # read in csv file
    headers = next(f)                     # grab the first line of headers
    for line in f:                        # loop thru lines and use values to 
        row = line.split(',')             # populate variables
        nshares = int(row[1])             # first value is number of shares
        price = float(row[2])             # 2nd value is price
        totalCost += nshares * price      # calculate cost of each stock and sum

print(f"Total cost of portfolio: {totalCost}")