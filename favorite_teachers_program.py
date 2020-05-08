#!/usr/bin/env python3

print("Welcome to the Favorite Teachers Program\n")

fav_teachers = []
fav_teachers.append(input("Who is your first favorite teacher: ").title())
fav_teachers.append(input("Who is your second favorite teacher: ").title())
fav_teachers.append(input("Who is your third favorite teacher: ").title())
fav_teachers.append(input("Who is your first favorite teacher: ").title())

# we don't need to create a new list to print out the alphabetical and reverse orders
# just operate on our list fav_teachers
print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse = True)))

print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.\n")

fav_teachers.insert(0, input("Oops, " + fav_teachers[0] + " is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title())

print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers, reverse = True)))

print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.\n")

# just like insert except we don't specify index, user does
fav_teachers.remove(input("You've decided you no longer like a teacher. Which teacher would you like to remove from your list").title())

print("\nYour favorite teachers ranked are: " + str(fav_teachers))
print("Your favorite teachers alphabetically are: " + str(sorted(fav_teachers)))
print("Your favorite teachers in reverse alphabetical order are: " + str(sorted(fav_teachers
, reverse = True)))

print("\nYour top two teachers are: " + fav_teachers[0] + " and " + fav_teachers[1] + ".")
print("Your next two favorite teachers are: " + fav_teachers[2] + " and " + fav_teachers[3] + ".")
print("Your last favorite teacher is: " + fav_teachers[-1] + ".")
print("You have a total of " + str(len(fav_teachers)) + " favorite teachers.\n")