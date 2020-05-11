#!/usr/bin/env python3

print("Welcome to the Voter Registration App\n")

name = str(input("Please enter your name: ")).strip().title()
age = int(input("Please enter your age: "))

parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

if age < 18:
	print("\nYou are not old enough to register to vote.")
else:
	print("\nCongratulations " + str(name) + "! You are old enough to register to vote. ")
	print("\nHere is a list of political parties to join.")
	for i in range(len(parties)):
		print("\t-" + parties[i])
	join = str(input("\nWhat party would you like to join: ")).strip().title()

	if join in parties:
		print("\nCongratulations " + str(name) + "! You have joined the " + join + " party!")
		if join == "Republican" or join == "Democratic":
			print("That is a majority party!")
		elif join == "Independent":
			print("You are an independent person!")
		else:
			print("That is not a major party.")
	else:
		print("That is not a given party.")
