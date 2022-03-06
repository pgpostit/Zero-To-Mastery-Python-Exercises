# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
print(basket)

# 1. Remove the Banana from the list
basket.remove('Banana')
print(f'1) {basket}')

# 2. Remove "Blueberries" from the list.
basket.pop(2)
print(f'2) {basket}')

# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
print(f'3) {basket}')

# 4. Add "Apples" at the beginning of the list
basket.insert(0, 'Apples')
print(f'4) {basket}')

# 5. Count how many apples in the basket
print(f'There is {basket.count("Apples")} apples on the Basket')

# 6. empty the basket
basket.clear()
print(f'6){basket}')