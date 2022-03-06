#find and print the duplicates in the following list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#1s solution:
secondlist = []
duplicates = []
for i in some_list:
    if i not in secondlist:
        secondlist.append(i)
    else:
        duplicates.append(i)

print(f'The list without the duplicates: {secondlist}')
print(f'The duplicates list: {duplicates}')