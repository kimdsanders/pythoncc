#4-13 Buffet

buffet_foods = ('bread', 'salad', 'steak', 'potatoes', 'cake')
for buffet_food in buffet_foods:
  print(buffet_food)

#try to modify the tuple, can't do it!!!!
buffet_foods.append('macaroni')

#make new tuple and loop thru
buffet_foods = ('bread', 'salad', 'beef', 'veggies', 'cake')
print("\nNew buffet menu: ")
for buffet_food in buffet_foods:
  print(buffet_food)
