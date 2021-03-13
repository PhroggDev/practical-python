# pcost.py
import csv
def portfolioCost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    totalCost = 0.0  # initiliaze a floating point variable
    with open(filename, 'rt') as f:  # read in csv file
        rows = csv.reader(f)
        headers = next(rows)                # grab the first line, headers
        for row in rows:                    # loop thru lines and use values
            try:
                nshares = int(row[1])       # first value is number of shares
                price = float(row[2])       # 2nd value is price
                totalCost += nshares * price  # calculate cost of each stock and sum
            except ValueError:  # catch missing or bad values
                print("Bad row: " + str(row))
    return totalCost
