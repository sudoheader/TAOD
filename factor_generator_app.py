#!/usr/bin/env python3

print("Welcome to the Factor Generator App\n")

flag = True


while flag:
	num = int(input("Enter a number to determine all factors of that number: "))
	factors = []
	for i in range(1, num + 1):
		if num % i == 0:
			factors.append(i)

	print("\nFactors of " + str(num) + " are: ")
	for factor in factors:
		print(factor)

	print("\nIn summary: ")
	for i in range(int(len(factors) / 2)):
		print(str(factors[i]) + " * " + str(factors[-i - 1]) + " = " + str(num))

	choice = input("\nRun again (y/n): ").lower()
	if choice != 'y':
		flag = False
		print("Thank you for using the program. Have a great day.")