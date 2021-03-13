symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')
# Use the in or not in operator to check if 'MSFT','AIG', and 'GOOG' are in the list of symbols.
for sym in ['MSFT', 'AIG', 'GOOG']:
    print(sym in symlist)
print('... and now if it is NOT')
for sym in ['MSFT', 'AIG', 'GOOG']:
    print(sym not in symlist)