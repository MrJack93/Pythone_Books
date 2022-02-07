
list_food = {}
for key in range(1, 5):
    food = input('Enter your favorite food: ')
    list_food[key] = food
print(list_food)
element = int(input('which element you want to exclude and remove it from the list: '))
del list_food[element]
sorted_tuple = sorted(list_food.items(), key=lambda x: x[1])
print(dict(sorted_tuple))
