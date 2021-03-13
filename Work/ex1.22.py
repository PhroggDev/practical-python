symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
# Append 'RHT'
symlist.append('RHT')
print(symlist)
# Insert 'AA' as the 2nd item in the list
symlist.insert(1, 'AA')
print(symlist)
# Remove 'MSFT'
symlist.remove('MSFT')
print(symlist)
# Append a new entry for 'YHOO'
symlist.append('YHOO')
print(symlist)
# Find the first instance of 'YHOO'
print(symlist.index('YHOO'))
# How many times does 'YHOO' appear in the list
print(symlist.count('YHOO'))
# Remove the first occurence of 'YHOO'
symlist.remove('YHOO')
print(symlist)