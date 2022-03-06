#Create a function to find the highest even in the following list: [10,1,2,3,4,8]

#My Solution
def highest_even(lista):
    even = []
    for i in lista:
        if i % 2 == 0:
            even.append(i)
    return max(even)


print(highest_even([10,1,2,3,4,8]))