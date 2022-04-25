# Exercise 1.28
#
# read text data from a gzipped CSV file
import gzip

with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
