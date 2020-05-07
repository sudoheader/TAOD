#!/usr/bin/env python3

import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

grocery = ['Meat', 'Cheese']

print("Welcome to the Grocery List App.")
print("Current Date and Time: " + str(month) + "/" + str(day) + " " + str(hour) + ":" + str(minute))
print("You currently have " + str(grocery[0]) + " and " + str(grocery[1]) + " in your list.\n")

food1 = str(input("Type of food to add to the grocery list: ").strip().title())
food2 = str(input("Type of food to add to the grocery list: ").strip().title())
food3 = str(input("Type of food to add to the grocery list: ").strip().title())
grocery.append(food1)
grocery.append(food2)
grocery.append(food3)

print("Here is your grocery list:")
print(str(grocery))
print("Here is your grocery list sorted:")
grocery.sort()
print(str(grocery))

print("\nSimulating grocery shopping...\n")

print("Current grocery list: " + str(len(grocery)) + " items")
print(str(grocery))
buy = str(input("What food did you just buy: ").title())
print("Removing " + buy + " from list...\n")
grocery.remove(buy)

print("Current grocery list: " + str(len(grocery)) + " items")
print(str(grocery))
buy = str(input("What food did you just buy: ").title())
print("Removing " + buy + " from list...\n")
grocery.remove(buy)

print("Current grocery list: " + str(len(grocery)) + " items")
print(str(grocery))
buy = str(input("What food did you just buy: ").title())
print("Removing " + buy + " from list...\n")
grocery.remove(buy)

print("Current grocery list: " + str(len(grocery)) + " items")
print(str(grocery))
out_of = grocery.pop()
print("\nSorry, the store is out of " + str(out_of) + ".")

instead = str(input("What food would you like instead: ").title())
grocery.insert(0, instead)
print("\nHere is what remains on your grocery list: ")
print(str(grocery))