#!/usr/bin/env python3

# fibonnacci function using list
# source: https://stackoverflow.com/a/18172463

print("Welcome to the Fibonacci Calculator App\n")
digits = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

seq = [1, 1]
for i in range(digits - 2):
	fib = seq[i] + seq[i + 1]
	seq.append(fib)

print("The first " + str(digits) + " numbers of the Fibonacci sequence are: ")
for i in seq:
	print(i)

val = []
for i in range(len(seq) - 1):
	r = seq[i + 1] / seq[i]
	val.append(r)

print("\nThe corresponding Golden Ratio values are: ")
for i in val:
	print(i)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")