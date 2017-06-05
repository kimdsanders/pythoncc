#4-12 More Loops

my_foods = ['pizza, 'falafel', 'carrot cake']
friends_foods = my_foods[:]

friends_foods.append('ice cream')

for my_food in my_foods:
  print(my_food)
  
for friends_food in friends_foods:
  print(friends_food)
