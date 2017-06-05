#5-2 More Conditional Tests

age = 25
if age >= 25
  print("You can rent a car.")
  print("Call 1-800-RENTAL")
else:
  print("Sorry, you're not old enough to rent a car.")
  print("Have your guardian call us!")
  
age = 32
if age > 18:
  print("You can drive. Renew your license every 3 years.")
elif age > 80:
  print("You can drive, but must renew your license annually.)
elif age < 18:
  print("You may drive along with a driver older than 18.")
elif age <15:
  print("You are not legally old enough to drive.")
  