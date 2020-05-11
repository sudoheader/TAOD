#!/usr/bin/env python3

print("Welcome to the Average Calculator App\n")

name = input("What is your name: ").strip().title()

num = int(input("How many grades would you like to enter: "))

grades = []
for i in range(num):
	grade = int(input("Enter grade: "))
	grades.append(grade)

print("\nGrades Highest to Lowest:")

grades.sort(reverse = True)
for i in range(num):
	print("\t" + str(grades[i]))

avg = sum(grades) / num
real_avg = avg

print("\n" + name + "'s Grade Summary:")
print("\tTotal Number of Grades: " + str(num))
print("\tHighest Grade: " + str(grades[0]))
print("\tLowest Grade: " + str(grades[-1]))
print("\tAverage: " + str(avg))

desired = float(input("\nWhat is your desired average: "))

needed = 50.0 # starting point
while avg < desired:
	grades.append(needed)
	num += 1 # remember to increase the number of scores when appending
	avg = sum(grades) / num
	if avg < desired:
		grades.remove(needed)
		num -= 1 # also when removing
		needed += 1 # iterate needed as needed ;-)

print("\nGood luck " + name + "!")
print("You will need to get a " + str(needed) + " on your next assignment to earn a " + str(desired) + " average.\n")

print("Lets see what your average could have been if you did better/worse on an assignment.")
change = int(input("What grade would you like to change: "))
change_to = int(input("What grade would you like to change " + str(change) + " to: "))

# remove needed
grades.pop()
grades = list(map(int, grades))

# Do the operation
new_grades = grades[:]
new_grades.remove(change)
new_grades.append(change_to)

print("\nNew Grades Highest to Lowest:")
new_grades.sort(reverse = True)
for i in range(len(new_grades)):
	print("\t" + str(new_grades[i]))

new_avg = sum(new_grades) / len(new_grades)

print("\n" + name + "'s New Grade Summary:")
print("\tTotal Number of Grades: " + str(len(new_grades)))
print("\tHighest Grade: " + str(int(new_grades[0])))
print("\tLowest Grade: " + str(int(new_grades[-1])))
print("\tAverage: " + str(round(new_avg, 1)))

print("\nYour new average would be a " + str(round(new_avg, 1)) + " compared to your real average of " + str(round(real_avg, 1)) + "!")
print("That is a change of " + str(round(new_avg - real_avg, 1)) + " points!")

print("\nToo bad your original grades are still the same!")
grades.sort(reverse = True)
print(str(grades))
print("You should go ask for extra credit!")