# pcost.py
#
# Exercise 1.33
# Reading file name(s) from the cli
import csv

f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
for row in rows:
    print(row)
f.close()
