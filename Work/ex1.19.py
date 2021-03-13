symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
# Split it into a list of names using the split() operation of strings:
symlist = symbols.split(',')
print(symlist)
# Some lookups 
print(symlist[0])
print(symlist[1])
print(symlist[2])
print(symlist[-1])
print(symlist[-2])
# Try reassigning one value:
symlist[2] = 'AIG'
print(symlist)
# Take a few slices:
print(symlist[0:3])
print(symlist[-2:])
# Make a new list and append an item to it
mysyms = []
mysyms.append('DOOG')
print(mysyms)
# You can reassign a portion of a list to another list. For example:
print(symlist)
symlist[-2:] = mysyms
print(symlist)