# report.py
#
# Exercise 2.4
import csv
# import sys


def read_portfolio(filename):
    with open(filename, 'r') as f:
        data = csv.DictReader(f)
        # print(line)
        # except ValueError:
        #     print('Missing or Bad value')
        return data
    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    # filename = 'Data/portfolio.csv'
