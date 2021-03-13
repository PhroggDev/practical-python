symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
# show symbols using only lower case
print(symbols.lower())
# assign symbols to a new variables using lower case letters
lowerCase = symbols.lower()
print(lowerCase)
# some more operations 
print(symbols.find('MSFT'))  # returns index of first char of found substring
print(symbols[13:17])  # print a slice of the symbols 
print(symbols.replace('SCO', 'DOA'))
# removing whitespace
name = '     IBM     \n'
print(name)
print(name.strip())