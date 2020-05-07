#!/usr/bin/env python3

import math

print("Welcome to the Multiplication/Exponent Table App")

name = (input("\nHello, what is your name: ")).strip().title()
num = float(input("What number would you like to work with: "))

print("\nMultiplication Table For " + str(num) + "\n")

# Multiplication table
for i in range(1, 10):
	i = float(i)
	prod = i * num
	print("\t" + str(i) + " * " + str(num) + " = " + str(round(prod, 2)))

print("\nExponent Table For " + str(num) + "\n")

for i in range(1, 10):
	exp = num ** i
	print("\t" + str(num) + " ** " + str(i) + " = " + str(round(exp, 4)))

cool = " Math is cool!"
print("\n" + name + cool)
print("\t" + name.lower() + cool.lower())
print("\t\t" + name + cool.title())
print("\t\t\t" + name.upper() + cool.upper())