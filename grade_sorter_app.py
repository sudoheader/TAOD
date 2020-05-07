#!/usr/bin/env python3

import math

print("Welcome to the Grade Sorter App\n")

first = int(input("What is your first grade (0-100): "))
second = int(input("What is your second grade (0-100): "))
third = int(input("What is your third grade (0-100): "))
fourth = int(input("What is your fourth grade (0-100): "))

grades = [first, second, third, fourth]
print("\nYour grades are: " + str(grades))
grades.sort(reverse = True)

print("\nYour grades from highest to lowest are: " + str(grades))

print("\nThe lowest two grades will now be dropped.")
low_grade1 = grades[-1]
low_grade2 = grades[-2]
print("Removed grade: " + str(low_grade1))
print("Removed grade: " + str(low_grade2))
remaining = grades[0:2]

print("\nYour remaining grades are: " + str(remaining))
print("Nice work! Your highest grade is a " + str(remaining[0]) + ".")