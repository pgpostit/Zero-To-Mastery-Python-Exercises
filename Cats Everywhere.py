#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Mia = Cat('Mia', 5)
Neneca = Cat('Neneca', 4)
Gatita = Cat('Gatita', 1)

# 2 Create a function that finds the oldest cat
def oldest_cat(*cats):
    Name = ''
    Age = 0
    for cat in cats:
        if cat.age > Age:
            Age = cat.age
            Name = cat.name
    old_data = [Name, Age]
    return old_data


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
ans = oldest_cat(Mia, Neneca, Gatita)
print(f'The oldest cat is {ans[0]} with {ans[1]} years old.')