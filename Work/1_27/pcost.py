# pcost.py
#
# Exercise 1.31
totalCost = 0


def portfolio_cost(filename):
    total = 0
    with open(filename, "rt") as f:
        headers = next(f).split(",")
        try:
            for line in f:
                row = line.split(",")
                nshares = int(row[1])
                price = float(row[2])
                total += nshares * price
        except:
            raise RuntimeError("Invalid or Missing value found")
        return total


cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: {cost:0.2f}")
