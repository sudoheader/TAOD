#!/usr/bin/env python3

print("\t\tSummary Table\n")

num_strings = ['15', '100', '55', '42']
print("The variable num_strings is a " + str(type(num_strings)) + ".")
print("It contains the elements: " + str(num_strings))
print("The element " + str(num_strings[0]) + " is a " + str(type(num_strings[0])) + ".\n")

num_ints = [15, 100, 55, 42]
print("The variable num_ints is a " + str(type(num_ints)) + ".")
print("It contains the elements: " + str(num_ints))
print("The element " + str(num_ints[0]) + " is a " + str(type(num_ints[0])) + ".\n")

num_floats = [2.2, 5.0, 1.245, 0.142857]
print("The variable num_floats is a " + str(type(num_floats)) + ".")
print("It contains the elements: " + str(num_floats))
print("The element " + str(num_floats[0]) + " is a " + str(type(num_floats[0])) + ".\n")

num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("The variable num_lists is a " + str(type(num_lists)) + ".")
print("It contains the elements: " + str(num_lists))
print("The element " + str(num_lists[0]) + " is a " + str(type(num_lists[0])) + "\n")

print("Now sorting num_strings and num_ints...")

num_strings.sort()
num_ints.sort()

print("Sorted num_strings: " + str(num_strings))
print("Sorted num_ints: " + str(num_ints))

print("\nStrings are sorted alphabetically while integers are sorted numerically!")