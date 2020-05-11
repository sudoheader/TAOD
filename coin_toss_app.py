#!/usr/bin/env python3

import random

print("Welcome to the Coin Toss App\n")

print("I will flip a coin a set number of times.")
num = int(input("How many times would you like me to flip the coin: "))
res = str(input("Would you like to see the result of each flip (y/n): ")).strip().lower()

print("\nFlipping!!!\n")

heads = 0
tails = 0

for flips in range(num):
	rand = random.randint(0, 1) # random number between 0 and 1
	if rand == 1:
		heads += 1
		if res.startswith("y"):
			print("HEADS")
	else:
		tails += 1
		if res.startswith("y"):
			print("TAILS")
	# can be heads or tails since they are equal
	if heads == tails:
		print("At " + str(flips + 1) + " flips, the number of heads and tails were equal at " + str(heads) + " each.")

print("\nResults Of Flipping A Coin " + str(num) + " Times:\n")
print("Side\t\tCount\t\tPercentage")
print("Heads\t\t" + str(heads) + "/" + str(num) + "\t\t" + str(round(100 * heads / num, 2)) + "%")
print("Tails\t\t" + str(tails) + "/" + str(num) + "\t\t" + str(round(100 * tails / num, 2)) + "%")