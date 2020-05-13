#!/usr/bin/env python3

print("Welcome to the Yes or No Issue Polling App\n")

issue = input("What is the yes or no issue you will be voting on the issue: ")
num = int(input("What is the number of voters you will allow on the issue: "))
password = input("Enter a password for polling results: ")

yes = 0
no = 0
# key = full_name, value = vote
results = { }

for i in range(num):
	full_name = input("\nEnter you full name: ").strip().title()
	if full_name in results.keys():
		print("Sorry, it seems that someone with that name has already voted.")
	else:
		print("Here is our issue: " + issue)
		vote = input("What do you think...yes or no: ").strip().lower()
		if vote == 'yes' or vote == 'y':
			yes += 1
			vote = 'yes'
		elif vote == 'no' or vote == 'n':
			no += 1
			vote = 'no'
		else:
			print("That is not a yes or no answer, but okay...")
		results[full_name] = vote
		print("Thank you " + full_name + "! Your vote of " + results[full_name] + " has been recorded.")

total = len(results.keys())
print("\nThe following " + str(total) + " people voted: ")
for key in results.keys():
	print(key)

print("\nOn the following issue: " + issue)
if yes > no:
	print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no > yes:
	print("No wins! " + str(no) + " votes to " + str(no) + ".")
else:
	print("It was a tie! " + str(no) + " votes to " + str(yes) + ".")

pw = input("\nTo see the voting results enter the admin password: ")
if pw == password:
	for key, value in results.items():
		print("Voter: " + key + "\t\t\tVote: " + value)
else:
	print("Sorry, that is not the correct password. Goodbye...")

print("\nThank you for using the Yes or No Issue Polling App.")