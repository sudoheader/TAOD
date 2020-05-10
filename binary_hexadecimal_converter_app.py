#!/usr/bin/env python3

print("Welcome to the Binary/Hexadecimal Converter App\n")

val = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
print("Generating lists....complete!\n")

print("Using slices, we will now show a portion of each list.")
start = int(input("What decimal number would you like to start at: "))
stop = int(input("What decimal number would you like to stop at: "))

decimal = list(range(1, val + 1))
print("\nDecimal values from " + str(start) + " to " + str(stop) + ":")
for i in range(start - 1, stop):
	print(decimal[i])

binary = []
hexadecimal = []
for i in decimal:
	binary.append(bin(i))
	hexadecimal.append(hex(i))
print("\nGenerating lists...Complete!")

print("\nBinary values from " + str(start) + " to " + str(stop) + ":")
for i in binary[start - 1:stop]:
	print(i)

print("\nHexadecimal values from " + str(start) + " to " + str(stop) + ":")
for i in hexadecimal[start - 1:stop]:
	print(i)

print("\nPress Enter to see all values from 1 to " + str(val) + ".")
print("Decimal" + "-"*4 + "Binary" + "-"*4 + "Hexadecimal")
print("-"*58)
for i, j, k in zip(decimal, binary, hexadecimal):
	print(str(i) + "-"*4 + str(j) + "-"*4 + str(k))