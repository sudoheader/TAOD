#!/usr/bin/env python3

import math

print("Welcome to the Right Triangle Solver App")

first = float(input("\nWhat is the first leg of the triangle: "))
second = float(input("What is the second leg of the triangle: "))

third = round(float(math.sqrt(first**2 + second**2)), 3)
area = round((first * second) / 2, 1)

print("\nFor a triangle with legs of " + str(first) + " and " + str(second) + " the hypotenuse is " + str(third) + ".")
print("For a triangle with legs of " + str(first) + " and " + str(second) + " the area is " + str(area) + ".")