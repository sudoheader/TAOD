#!/usr/bin/env python3

print("W​elcome to the Basketball Roster Program\n")

pg = str(input("Who is your point guard: ").strip().title())
sg = str(input("Who is your shooting guard: ").strip().title())
sf = str(input("Who is your small forward: ").strip().title())
pf = str(input("Who is your power forward: ").strip().title())
ce = str(input("Who is your center: ").strip().title())
roster = [pg, sg, sf, pf, ce]

print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard: \t\t" + roster[0])
print("\t\tShooting Guard: \t" + roster[1])
print("\t\tSmall Forward: \t\t" + roster[2])
print("\t\tPower Forward: \t\t" + roster[3])
print("\t\tCenter: \t\t" + roster[4])

# pop injured_player from roster
injured_player = roster[2]
roster.pop(2)

print("\nOh no, " + str(injured_player) + " is injured.")
print("Your roster only has " + str(len(roster)) + " players.")

# insert added_player to roster at position sf
added_player = str(input("Who will take " + str(injured_player) + "'s spot: ").strip().title())
roster.insert(2, added_player)

print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard: \t\t" + roster[0])
print("\t\tShooting Guard: \t" + roster[1])
print("\t\tSmall Forward: \t\t" + roster[2])
print("\t\tPower Forward: \t\t" + roster[3])
print("\t\tCenter: \t\t" + roster[4])

print("\nGood luck " + str(added_player) + " you will do great!")
print("Your roster now has " + str(len(roster)) + " players.")