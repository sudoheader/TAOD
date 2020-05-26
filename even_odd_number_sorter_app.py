#!/usr/bin/env python3

print("Welcome to the Even Odd Number Sorter App\n")

running = True

numbers = input("Enter in a string of numbers separated by a comma (,) : ").replace(" ", "")
num_list = numbers.split(",")
print(num_list)

evens = []
odds = []

print("---- Result Summary ----")

for i in range(len(num_list)):
	if num_list[i] % 2 == 0:
		evens.append(i)
		print("\t" + str(num_list[i]) + " is even!")
	else:
		odds.append(i)
		print("\t" + str(num_list[i]) + " is odd!")

evens.sort()
odds.sort()
print("The following " + str(evens.count()) + " numbers are even:")
for i in evens:
	print("\t" + evens[i])
# for i in lstEven:

print("The following " + str(odds.count()) + " numbers are odd:")
for i in odds:
	print("\t" + odds[i])