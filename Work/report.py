# report.py
#
# Exercise 2.4
import csv
# import sys


def read_portfolio(filename):
    portfolio = {}
    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            print(line)
        # except ValueError:
        #     print('Missing or Bad value')
    return portfolio
    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    # filename = 'Data/portfolio.csv'
