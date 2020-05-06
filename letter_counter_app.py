#!/usr/bin/env python3

print("Welcome to the Letter Counter App\n")

name = input("What is your name: ").title().strip()

print("Hello " + name + "!")
print("I will count the number of times that a specific letter occurs in a message.\n")

message = input("Please enter a message: ").lower()
letter = input("Which letter would you like to count the occurrences of: ").lower()
count = message.count(letter)

print("\n" + name + ", your message has " + str(count) + " " + letter + "'s in it.")