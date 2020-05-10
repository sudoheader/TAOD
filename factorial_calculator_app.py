#!/usr/bin/env python3

import math

print("Welcome to the Factorial Calculator App\n")

num = int(input("What number would you like to compute the factorial of? "))

print(str(num) + "! = ", end = "")
for i in range(1, num):
	print(str(i), end = " * ")
print(str(num))

# using math library
fact = math.factorial(num)
print("Here is the result from the math library: ")
print("The factorial of " + str(num) + " is " + str(fact) + "!\n")

print("Here is the result from my own algorithm: ")

# with inefficient function factorial
def factorial(n):
	if n == 0 or n == 1: return 1
	else: return n * factorial(n - 1)

own_fact = factorial(num)

print("The factorial of " + str(num) + " is " + str(own_fact) + "!\n")
print("It is shown twice that " + str(num) + "! = " + str(own_fact) + " (with excitement)")
