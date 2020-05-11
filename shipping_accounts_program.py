#!/usr/bin/env python3

print("Welcome to the Shipping Accounts Program\n")

users = ['eramom', 'footea', 'davisv', 'papinukt', 'allenj']

username = str(input("Hello, what is your username: ")).strip().lower()

# if not in list exit program
if username not in users:
	print("Sorry, you do not have an account with us. Goodbye.")
	exit()

print("Hello " + username + ". Welcome back to your account.")
print("Current shipping prices are as follows:\n")

print("Shipping orders 0 to 100:\t\t$5.10 each")
print("Shipping orders 100 to 500:\t\t$5.00 each")
print("Shipping orders 500 to 1000:\t\t$4.95 each")
print("Shipping orders over 1000:\t\t$4.80 each")
ship = int(input("\nHow many items would you like to ship: "))

small = 5.10
medium = 5.00
large = 4.95
larger = 4.80

# logic for calculating cost could be better
if ship < 100:
	per = small
	cost = per * ship
elif ship < 500:
	per = medium
	cost = per * ship
elif ship < 1000:
	per = large
	cost = per * ship
else:
	per = larger
	cost = per * ship

print("To ship " + str(ship) + " items it will cost you " + "$" + str(round(cost, 2)) + " at $" + str(per) + " per item.")

place = str(input("\nWould you like to place this order (y/n): ")).lower()

if place == "y":
	print("Okay, shipping your " + str(ship) + " items.")
elif place == "n":
	print("Okay, no order is being placed at this time.")
