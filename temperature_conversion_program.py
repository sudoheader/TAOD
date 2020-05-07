#!/usr/bin/env python3

print("Welcome to the Temperature Conversion Program")

fahrenhiet = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))

celsius = (fahrenhiet - 32) * 5 / 9
kelvin = celsius + 273.15

print("\nDegrees Fahrenheit:\t" + str(fahrenhiet))
print("Degrees Celsius:\t" + str("{:.4f}".format(celsius)))
print("Degrees Kelvin:\t\t" + str("{:.4f}".format(kelvin)))