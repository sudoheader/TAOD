#!/usr/bin/env python3

print("Welcome to the Database Admin Program\n")

log_on_information = {
	'mooman74':'alskes145',
	'meramo1986':'kehns010101',
	'nickyD':'world1star',
	'george2':'booo3oha',
	'admin00':'admin1234'
}

username = input("Enter your username: ")

if username in log_on_information.keys():
	# very bad way of storing passwords (DO NOT REPEAT)
	password = input("Enter your password: ")

	if password == log_on_information[username]:
		print("\nHello " + username + "! You are logged in!")

		# admin should NOT be able to see passwords as well but we do it here anyway
		if username == "admin00": # admin00
			print("\nHere is the current user database:")
			for key, value in log_on_information.items():
				print("Username: " + key + "\t\t" + "Password: " + value)
		else:
			choice = input("Would you like to change your password: ").strip().lower()
			if choice.startswith("y"):
				change = input("What would you like your new password to be: ")
				if len(change) >= 8:
					# also do NOT needlessly print out the user's password in plain text
					log_on_information[username] = change
				else:
					print(str(change) + " not the minimum eight characters.")
				print("\n" + username + " your password is " + log_on_information[username] + ".")
			else:
				print("\nThank you, goodbye.")
	else:
		print("Password incorrect!	")
else:
	print("Username not in database, goodbye.")