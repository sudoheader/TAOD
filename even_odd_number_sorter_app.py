#!/usr/bin/env python3

print("Welcome to the Even Odd Number Sorter App\n")

running = True

while running:
	numbers = input("Enter in a string of numbers separated by a comma (,) : ").replace(" ", "")
	num_list = numbers.split(",")

	evens = []
	odds = []

	print("\n---- Result Summary ----")

	# test if number is even or odd
	for i in range(len(num_list)):
		i = int(i)
		if i % 2 == 0:
			evens.append(i)
			print("\t" + str(i) + " is even!")
		else:
			odds.append(i)
			print("\t" + str(i) + " is odd!")

	# sort lists
	evens.sort()
	odds.sort()
	print("\nThe following " + str(len(evens)) + " numbers are even:")
	for i in evens:
		print("\t" + str(i))

	print("\nThe following " + str(len(odds)) + " numbers are odd:")
	for i in odds:
		print("\t" + str(i))

	# stop loop if choice is 'y'
	choice = input("\nWould you like to run the program again (y/n): ").lower()
	if choice != 'y':
		running = False
		print("Thank you for using the program. Goodbye.")