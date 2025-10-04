empty = ()
brothers = ('max', 'guy', 'nathan', 'alexander')
sisters = ('grace', 'nathalie', 'olivia', 'mariana')
siblings =  brothers + sisters
print(siblings)
print(len(siblings))
list_siblings = list(siblings)
parents = ('father', 'mother')
family = list_siblings + (list(parents))
print(family)



*siblings, father, mother = family
parents = [father, mother]
print(parents)
print(siblings)
fruits = ('apple', 'banana', 'dragon fruit', 'orange')
vegetables = ('lettuce', 'cabbage', 'cucumber', 'onion')
animals = ('hamster', 'beef', 'pork', 'chicken')
food_stuff_tp = fruits +  vegetables + animals
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(len(food_stuff_lt))
sliced_food_stuff_lt = food_stuff_lt[0:6:1] + food_stuff_lt[7:13:1]
print(sliced_food_stuff_lt)
three_sliced_food_stuff_lt = sliced_food_stuff_lt[3:8]
print(three_sliced_food_stuff_lt)
del food_stuff_tp
'apple' in food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
Estonia
