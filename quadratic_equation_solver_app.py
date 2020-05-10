#!/usr/bin/env python3

import cmath

print("Welcome to the Quadratic Equation Solver App.\n")

print("A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n")

equations = int(input("How many equations would you like to solve today: "))

# for loop for number of equations
for i in range(equations):
	print("\nSolving equation #" + str(i + 1))
	print("-"*63 + "\n")
	a = float(input("Please enter your value of a (coefficient of x^2): "))
	b = float(input("Please enter your value of b (coefficient of x): "))
	c = float(input("Please enter your value of c (coefficient): "))

	print("\nThe solutions to " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0 are:")

	# using quadratic formula
	# x = (-b +/- sqrt(b^2 - 4ac)) / (2a)
	sqrt_dis = cmath.sqrt(b**2 - 4 * a * c) # square root of discriminant
	x1 = (-b + sqrt_dis) / (2 * a)
	x2 = (-b - sqrt_dis) / (2 * a)
	# cmath allows us to output with complex numbers
	print("\n\tx1 = " + str(x1))
	print("\tx2 = " + str(x2))

print("\nThank you for using the Quadratic Equation Solver App. Goodbye.")
