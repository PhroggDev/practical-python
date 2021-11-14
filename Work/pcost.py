# pcost.py
#
# Exercise 1.27
# import csv
import sys
from report import read_portfolio


def portfolioCost(filename):
    totalCostDict = read_portfolio(filename)
    return totalCostDict
# print(f'Total cost: {portfolioCost('Data/portfolio.csv'):.2f}')


# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
myFilename = 'Data/portfolio.csv'
costDict = portfolioCost(myFilename)
print(costDict)
