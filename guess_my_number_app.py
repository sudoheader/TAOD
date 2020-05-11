#!/usr/bin/env python3

import random

print("Welcome to the Guess My Number App\n")

name = str(input("Hello! What is your name: ").strip().title())
print("Well " + str(name) + ", I am thinking of a number between 1 and 20.\n")

rand = random.randint(1, 20)

for guesses in range(5):
	guess = int(input("Take a guess: "))
	if guess > rand:
		print("Your guess is too high.\n")
	elif guess < rand:
		print("Your guess is to low.\n")
	else:
		break

if guess == rand:
	print("\nGood job, " + str(name) + "! You guessed my number in " + str(guesses + 1) + " guesses! ")
else:
	print("Game Over. The number I was thinking of was " + str(rand) + ".")