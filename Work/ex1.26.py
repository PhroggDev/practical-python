import os
d = os.getcwd()
print(d)
# read entire file and spit it out
with open('Data/portfolio.csv', 'rt') as f:
    data = f.read()
print(data)
# read file and spit it out line by line
with open('Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line, end='')
# read file * grap first line into a var * spit out the rest line by line
f = open('Data/portfolio.csv', 'rt')
headers = next(f)
print(f"The first line is ==> {headers}")
print("The rest of the file follows...")
for line in f:
    print(line, end='')
f.close()

