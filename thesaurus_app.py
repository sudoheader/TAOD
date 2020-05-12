#!/usr/bin/env python3

import random

thesaurus = {
	"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
	"cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
	"happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
	"sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print("Welcome to the Thesaurus App!\n")

print("Choose a word from the thesaurus and I will give you a synonym.\n")
print("Here are the words in the thesaurus:")
for keys in thesaurus.keys():
	print("\t-" + keys)

word = str(input("What word would you like a synonym for: ")).strip().lower()

if keys in thesaurus.keys():
	rand = random.randint(0, 4) # use random to get a random synonym
	print("A synonym for " + keys + " is " + thesaurus[keys][rand] + ".")
else:
	print("I'm sorry, that word is not currently in the thesaurus.")

choice = str(input("\nWould you like to see the whole thesaurus (yes/no): ")).strip().lower()
if choice.startswith("y"):
	for key, values in thesaurus.items():
		print("\n" + key.title() + " synonyms are: ")
		for value in values:
			print("\t-" + value)
else:
	print("\nI hope you enjoyed the program. Thank you!")
