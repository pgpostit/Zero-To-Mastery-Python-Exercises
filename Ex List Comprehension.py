#Use list comprehension to find the duplicates again
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
print(list(set([x for x in some_list if some_list.count(x)>1])))
