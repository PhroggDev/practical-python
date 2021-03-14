from pcost import portfolioCost
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
cost = portfolioCost(filename)
print(f"Total Cost: {cost}")