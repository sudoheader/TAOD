#!/usr/bin/env python3

print("Welcome to the MPH to MPS Conversion App\n")

speed = float(input("What is your speed in miles per hour: "))

mps = speed * 0.4474
mps = round(mps, 2)
# mps = "{:.2f}".format(mps)

print("Your speed in meters per second is " + str(mps) + ".")