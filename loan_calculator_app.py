#!/usr/bin/env python3

from matplotlib import pyplot

def get_loan_info():
	"""Get the basic information of a loan and store it in a dictionary"""
	loan = {}
	loan['principal'] = float(input("Enter the loan amount: "))
	loan['rate'] = float(input("Enter the interest rate: "))/100
	loan['monthly payment'] = float(input("Enter the desired monthly payment amount: "))
	loan['money paid'] = 0
	return loan

def show_loan_info(loan, number):
	"""Display the current loan status"""
	print("\n----Loan information after " + str(number) + " months----")
	for key, value in loan.items():
		print(key.title() + ": " + str(value))

def collect_interest(load):
	"""Update load for interest per month"""
	loan['principal'] = loan['principal'] + loan['principal'] / 12

def make_monthly_payment(loan):
	"""Simulate making a monthly payment to pay down the principal"""
	loan['principal'] = loan['principal'] - loan['monthly payment']

	if loan['principal'] > 0:
		loan['money paid'] += loan['monthly payment']
	else:
		loan['money paid'] += loan['monthly payment'] + loan['principal']
		loan['principal'] = 0

def summarize_loan(loan, number, initial_principal):
	"""Display the results of paying off the loan"""
	print("\nCongraulations!  You paid off your loan in " + str(number) + " months!")
	print("Your initial loan was $" + str(initial_principal) + " at a rate of " + str(100 * loan['rate']) + "%.")
	print("Your monthly payment was $" + str(loan['monthly payment']) + ".")
	print("You spent $" + str(round(loan['money paid'], 2)) + " in total.")
	interest = round(loan['money paid'] - initial_principal, 2)
	print("You spent $" + str(interest) + " on interest!")

def create_graph(data, loan):
	"""Create a graph to show the relationship between principal and time"""
	x_values = []
	y_values = []

	for point in data:
		x_values.append(point[0])
		y_values.append(point[1])
	pyplot.plot(x_values, y_values)
	pyplot.title(str(100 * loan['rate']) + "% Interest With $" + str(loan['monthly payment']) + " Monthly Payment")
	pyplot.xlabel("Month Number")
	pyplot.ylabel("Principal of Loan")
	pyplot.show()

print("Welcome to the Loan Calculator App\n")

month_number = 0
my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []

show_loan_info(my_loan, month_number)
input("Press 'Enter' to begin paying off your loan.")

while my_loan['principal'] > 0:
	if my_loan['principal'] > starting_principal:
		break
	month_number += 1
	collect_interest(my_loan)
	make_monthly_payment(my_loan)
	data_to_plot.append((month_number, my_loan['principal']))
	show_loan_info(my_loan, month_number)

if my_loan['principal'] <= 0:
	summarize_loan(my_loan, month_number, starting_principal)
	create_graph(data_to_plot, my_loan)
else:
	print("\nYou will NEVER pay off your loan!!!")
	print("You cannot get ahead of the interest! :-(")