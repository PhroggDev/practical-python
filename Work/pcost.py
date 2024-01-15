# pcost.py
#
# Exercise 1.32
import csv

f = open("Work/Data/portfolio.csv")
rows = csv.reader(f)
headers = next(rows)
print(headers)
for row in rows:
    print(row)
f.close()
