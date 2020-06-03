#!/usr/bin/env python3

def get_info():
	"""Get user information to store in a dict that represents a bank account"""
	print("Welcome to the Python First National Bank.")
	name = input("\nHello, what is your name: ").title().strip()
	savings = int(input("How much money would you like to set up your savings account with: "))
	checking = int(input("How much money would you like to set up your checking account with: "))
	bank_account = {
		"Name":name,
		"Savings":savings,
		"Checking":checking,
		}
	return bank_account

def make_deposit(bank_account, account, money):
	"""Add money to a specific type of account"""
	bank_account[account] += money
	print("\nDeposited $" + str(money) + " into " + bank_account['Name'] + "'s " + account.lower() + " account.")

def make_withdrawal(bank_account, account, money):
	"""Withdraw money from a specific type of account"""
	if bank_account[account] - money >= 0:
		bank_account[account] -= money
		print("\nWithdrew $" + str(money) + " from " + bank_account['Name'] + "'s " + account.lower() + " account.")
	else:
		print("\nSorry, by withdrawing $" + str(money) + " you will have a negative balance.")

def display_info(bank_account):
	"""Display all key-value pairs in a given bank account"""
	print("\nCurrent Account Information")
	for key, value in bank_account.items():
		if key == 'Name':
			print(key + ": " + str(value))
		else:
			print(key + ": $" + str(value))

my_account = get_info()

running = True
while running:
	display_info(my_account)

	account_type = input("\nWhat account would you like to access (Savings or Checking): ").title()
	choice = input("What type of transaction would you like to make (Deposit or Withdrawal): ").title()
	amount = float(input("How much money: "))

	if account_type == "Savings" or account_type == "Checking":
		if choice == "Deposit":
			make_deposit(my_account, account_type, amount)
		elif choice == "Withdrawal":
			make_withdrawal(my_account, account_type, amount)
		else:
			print("\nI'm sorry, we cannot do that for you today.")
	else:
		print("\nI'm sorry, we cannot do that for you today.")

	choice = input("Would you like to make another transaction (y/n): ").lower()
	if choice != 'y':
		display_info(my_account)
		print("\nThank you. Have a great day!")
		running = False