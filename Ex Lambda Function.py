#Create a lambda function to return square of the numbers in a list
print(list(map(lambda num: num**2, [1,2,3])))


#Sort this list
a=[(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)